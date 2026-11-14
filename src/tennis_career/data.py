import requests
import pandas as pd
import json
from datetime import datetime


def download_player_data(player_name):
    name = "".join(word.capitalize() for word in player_name.split())
    url = f"https://www.tennisabstract.com/jsmatches/{name}Career.js"

    response = requests.get(url, timeout=60)

    if response.status_code != 200 or "morematchmx" not in response.text:
        raise ValueError(f"Could not find career data for '{player_name}'")

    return response.text
def parse_match_data(js_text):
    start = js_text.find("[[", js_text.find("morematchmx"))

    if start == -1:
        raise ValueError("Could not find match data")

    matches, _ = json.JSONDecoder().raw_decode(js_text[start:])
    df = pd.DataFrame(matches)

    return df
def calculate_age(match_date, birth_date):
    match = datetime.strptime(str(match_date), "%Y%m%d")
    birth = datetime.strptime(str(birth_date), "%Y%m%d")
    return (match - birth).days / 365.25
def clean_match_data(df, birth_date, gender):
    df = df.copy()
    df["DATE"] = pd.to_datetime(df[0], format="%Y%m%d", errors="coerce")
    df["PLAYER_AGE"] = df[0].apply(
        lambda date: calculate_age(date, birth_date)
    )

    if gender == "female":
        df["OPP_AGE"] = df.apply(
            lambda row: calculate_age(row[0], row[16])
            if pd.notna(row[16]) and str(row[16]).isdigit() else None,
            axis=1
        )
    else:
        df["OPP_AGE"] = pd.to_numeric(df[16], errors="coerce")

    df["AGE_DIFF"] = df["PLAYER_AGE"] - df["OPP_AGE"]
    df["W/L"] = df[4]

    return df[["DATE", "PLAYER_AGE", "OPP_AGE", "AGE_DIFF", "W/L"]].dropna()