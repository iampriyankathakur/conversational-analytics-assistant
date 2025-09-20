import re

def parse_query(query):
    query = query.lower()
    if "average income" in query and "city" in query:
        return {"action": "groupby_mean", "column": "income", "by": "city"}
    elif "count" in query and "city" in query:
        return {"action": "groupby_count", "column": "id", "by": "city"}
    else:
        return {"action": "summary"}
