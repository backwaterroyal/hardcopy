import httpx

ENDPOINT = "https://api.hardcover.app/v1/graphql"

_FOLLOWED_BOOKS_QUERY = """
{
  me {
    follows(where: { followable_type: { _eq: "Book" } }) {
      book { title }
    }
  }
}
"""

_BOOKS_IN_SERIES_QUERY = """
query BooksInSeries($id: Int!) {
  book_series(
    distinct_on: position
    order_by: [{ position: asc }, { book: { users_count: desc } }]
    where: {
      series_id: { _eq: $id }
      compilation: { _eq: false }
      book: {
        canonical_id: { _is_null: true }
        is_partial_book: { _eq: false }
      }
    }
  ) {
    book { title }
  }
}
"""


def _post(api_key: str, query: str, variables: dict | None = None) -> dict:
    response = httpx.post(
        ENDPOINT,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"query": query, "variables": variables or {}},
        timeout=30.0,
    )
    response.raise_for_status()
    payload = response.json()
    if "errors" in payload:
        raise RuntimeError(f"hardcover graphql errors: {payload['errors']}")
    return payload["data"]


def get_followed_books(api_key: str) -> list[str]:
    data = _post(api_key, _FOLLOWED_BOOKS_QUERY)
    me = data["me"]
    if not me:
        return []
    return [
        f["book"]["title"]
        for f in me[0]["follows"]
        if f.get("book") and f["book"].get("title")
    ]


def get_books_in_a_series(api_key: str, series_id: str) -> list[str]:
    data = _post(api_key, _BOOKS_IN_SERIES_QUERY, {"id": int(series_id)})
    return [
        row["book"]["title"]
        for row in data["book_series"]
        if row.get("book") and row["book"].get("title")
    ]
