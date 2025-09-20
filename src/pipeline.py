import argparse, pandas as pd
from query_parser import parse_query
from analyzer import run_analysis
from visualizer import visualize

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to dataset CSV")
    parser.add_argument("--query", required=True, help="Natural language query")
    args = parser.parse_args()

    df = pd.read_csv(args.file)
    parsed = parse_query(args.query)
    result = run_analysis(df, parsed)

    print("✅ Answer:")
    print(result)

    chart_path = visualize(result)
    if chart_path:
        print(f"📊 Chart saved at {chart_path}")
