# SPEC - HardcoverHandler

Python module for the hardcover.app graphql api.

## G - goal

fetch data from hardcover using a passed key.

## C - constraints
- C1: python, self contained module
- C2: use httpx for requests
- C3: output is a list of books

## I - interfaces
- I.api: get_followed_books(api_key: str) -> list[book: str]
- I.endpoint: https://api.hardcover.app/v1/graphql

## V - invariants

## T - tasks
| id | st | desc | cites |
|----|----|----|----|
| t1 | x | scaffold module | C1 |
| t2 | x | implement followed books function | I.api |

## B - bugs
| id | date | cause | fix |
|----|----|----|----|

