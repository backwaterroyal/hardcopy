# SPEC - HardcoverHandler

Python module for the hardcover.app graphql api.

## G - goal

fetch data from hardcover using a passed key.

## C - constraints
- C1: python, self contained module
- C2: use httpx for requests
- C3: output is a list of books
- C4: write only in the HardcoverHandler folder excepting adding packages

## I - interfaces
- I.api: get_followed_books(api_key: str) -> list[book: str]
- I.endpoint: https://api.hardcover.app/v1/graphql

## V - invariants
- V1: write integration tests, but not unit tests.

## T - tasks
| id | st | desc | cites |
|----|----|----|----|
| t1 | x | scaffold module | C1 |
| t2 | x | implement followed books function | I.api |
| t3 | x | integration test for existing code | V1
| t4 | x | fix query to me.follows where followable_type=Book | I.api,B1 |

## B - bugs
| id | date | cause | fix |
|----|----|----|----|
| b1 | 2026-04-30 | used root `followed_user_books`; returned empty for real users. follow data lives in polymorphic `follows` scoped via `me` filtered by followable_type=Book | t4 |

