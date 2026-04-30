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
- I.api: get_books_in_a_series(api_key: str, series_id: str) - list[book: str]

## V - invariants
- V1: write integration tests, but not unit tests.

## T - tasks
| id | st | desc | cites |
|----|----|----|----|
| t1 | x | scaffold module | C1 |
| t2 | x | implement followed books function | I.api |
| t3 | x | integration test for existing code | V1
| t4 | x | fix query to me.follows where followable_type=Book | I.api,B1 |
| t5 | x | add function to get the books in series | I.api |
| t6 | x | expand get followed books function to fetch followed series, and then get all the books that make up those series | I.api |
| t7 | x | filter position is_null=false in books-in-series query | I.api,b2 |

## B - bugs
| id | date | cause | fix |
|----|----|----|----|
| b1 | 2026-04-30 | used root `followed_user_books`; returned empty for real users. follow data lives in polymorphic `follows` scoped via `me` filtered by followable_type=Book | t4 |
| b2 | 2026-04-30 | books_in_series included greek translation; position-null row bypassed distinct_on dedup. distinct_on does not collapse multi-null buckets | t7 |

