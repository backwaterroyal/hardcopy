import os

import pytest

from hardcopy.HardcoverHandler import get_books_in_a_series, get_followed_books


def test_get_followed_books_real():
    key = os.environ.get("HARDCOVER_API_KEY")
    if not key:
        pytest.skip("HARDCOVER_API_KEY not set")
    books = get_followed_books(key)
    assert isinstance(books, list)
    assert all(isinstance(b, str) for b in books)


def test_get_books_in_a_series_real():
    key = os.environ.get("HARDCOVER_API_KEY")
    series_id = os.environ.get("HARDCOVER_TEST_SERIES_ID")
    if not key or not series_id:
        pytest.skip("HARDCOVER_API_KEY or HARDCOVER_TEST_SERIES_ID not set")
    books = get_books_in_a_series(key, series_id)
    assert isinstance(books, list)
    assert all(isinstance(b, str) for b in books)
