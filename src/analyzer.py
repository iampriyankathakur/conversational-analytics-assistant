import pandas as pd

def run_analysis(df, parsed_query):
    if parsed_query["action"] == "groupby_mean":
        return df.groupby(parsed_query["by"])[parsed_query["column"]].mean()
    elif parsed_query["action"] == "groupby_count":
        return df.groupby(parsed_query["by"])[parsed_query["column"]].count()
    elif parsed_query["action"] == "summary":
        return df.describe()
