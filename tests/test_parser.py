from src.query_parser import parse_query

def test_parse_query():
    query = "What is the average income by city?"
    parsed = parse_query(query)
    assert parsed["action"] == "groupby_mean"
    assert parsed["column"] == "income"
    assert parsed["by"] == "city"
