import os

import pytest

from hardcopy.HardcoverHandler import get_followed_books


def test_get_followed_books_real():
    key = os.environ.get("HARDCOVER_API_KEY")
    if not key:
        pytest.skip("HARDCOVER_API_KEY not set")
    books = get_followed_books(key)
    assert isinstance(books, list)
    assert all(isinstance(b, str) for b in books)
