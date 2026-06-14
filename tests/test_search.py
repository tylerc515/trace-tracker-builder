"""Tests for the shared text search/filter helper."""

from app.search import matches_search


def test_empty_query_matches_everything():
    assert matches_search("", "International Paper", "Mansfield")


def test_single_term_matches_any_field_case_insensitively():
    assert matches_search("mansfield", "International Paper", "Mansfield")
    assert not matches_search("mansfield", "International Paper", "Riverside")


def test_multiple_terms_require_all_to_match_some_field():
    assert matches_search("international rb2", "International Paper", "Recovery Boiler #2 (RB2)")
    assert not matches_search("international rb3", "International Paper", "Recovery Boiler #2 (RB2)")


def test_term_can_match_substring_within_field():
    assert matches_search("mans", "International Paper", "Mansfield")
