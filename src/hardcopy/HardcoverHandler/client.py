import httpx

ENDPOINT = "https://api.hardcover.app/v1/graphql"

_QUERY = "{ followed_user_books { book { title } } }"


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
    rows = payload["data"]["followed_user_books"]
    return [row["book"]["title"] for row in rows if row.get("book") and row["book"].get("title")]
