import pytest
from tennis_career.data import parse_match_data, clean_match_data


female_js = """
var morematchmx = [
["19951030", "Canadian Open", "Carpet", "W", "L",
"", "", "WC", "Q1", "6-1 6-1", "3",
"Anne Miller", "149", "7", "", "R",
"19770119", "", "USA", "0"]
]
"""

male_js = """
var morematchmx = [
["20010910", "Spain F10", "Hard", "S", "L",
"", "", "WC", "R32", "2-6 7-5 6-2", "3",
"Guillermo Platel", "731", "", "", "R",
"22.264202601", "", "ESP", "0"]
]
"""


def test_parse_female():
    df = parse_match_data(female_js)
    assert len(df) == 1
    assert df.iloc[0, 11] == "Anne Miller"


def test_parse_male():
    df = parse_match_data(male_js)
    assert len(df) == 1
    assert df.iloc[0, 11] == "Guillermo Platel"


def test_clean_female():
    df = parse_match_data(female_js)
    clean = clean_match_data(df, "19810926", "female")
    assert len(clean) == 1
    assert clean.iloc[0]["W/L"] == "L"
    assert clean.iloc[0]["PLAYER_AGE"] == pytest.approx(14.09, abs=0.02)


def test_clean_male():
    df = parse_match_data(male_js)
    clean = clean_match_data(df, "19860603", "male")
    assert len(clean) == 1
    assert clean.iloc[0]["OPP_AGE"] == pytest.approx(22.264, abs=0.01)