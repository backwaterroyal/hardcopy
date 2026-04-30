import json
import os

import httpx

key = os.environ["HARDCOVER_API_KEY"]
query = """
{
  me {
    id
    username
    follows(where: { followable_type: { _eq: "Book" } }) {
      book { title }
    }
  }
}
"""
r = httpx.post(
    "https://api.hardcover.app/v1/graphql",
    headers={"Authorization": f"Bearer {key}"},
    json={"query": query},
)
print(json.dumps(r.json(), indent=2))
