import pandas as pd


def get_top_k_players(
    df: pd.DataFrame,
    stat_col: str,
    k: int,
) -> pd.DataFrame:
    filtered_df = df.nlargest(k, stat_col)

    return filtered_df[["Player", stat_col]]




# schedule = bbref_api.get_table("teams/NYK/2026_games")
# today = datetime.now().date()
# schedule["date"] = schedule["Date"].apply(lambda x: datetime.strptime(x, "%a, %b %d, %Y")).dt.date
# schedule[
#     (schedule["date"] >= today - timedelta(days=1))
#     & (schedule["date"] <= today + timedelta(days=1))
# ]