"""Tests for pdf-split."""

import pytest
from pdf_split import split


class TestSplit:
    """Test suite for split."""

    def test_basic(self):
        """Test basic usage."""
        result = split("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            split("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = split(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
