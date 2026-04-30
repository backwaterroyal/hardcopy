import httpx

ENDPOINT = "https://api.hardcover.app/v1/graphql"

_QUERY = """
{
  me {
    follows(where: { followable_type: { _eq: "Book" } }) {
      book { title }
    }
  }
}
"""


def get_followed_books(api_key: str) -> list[str]:
    response = httpx.post(
        ENDPOINT,
        headers={"Authorization": f"Bearer {api_key}"},
        json={"query": _QUERY},
        timeout=30.0,
    )
    response.raise_for_status()
    payload = response.json()
    if "errors" in payload:
        raise RuntimeError(f"hardcover graphql errors: {payload['errors']}")
    me = payload["data"]["me"]
    if not me:
        return []
    return [
        f["book"]["title"]
        for f in me[0]["follows"]
        if f.get("book") and f["book"].get("title")
    ]
