import argparse
from openllm import *


def main():
    parser = argparse.ArgumentParser(description="Scrape and export data from the Hugging Face leaderboard")
    parser.add_argument("-csv", action="store_true", help="Export data to CSV")
    parser.add_argument("-html", action="store_true", help="Export data to HTML")
    parser.add_argument("-json", action="store_true", help="Export data to JSON")
    
    args = parser.parse_args()

    data = get_json_format_data()
    finished_models = get_datas(data)
    df = pd.DataFrame(finished_models)

    if not args.csv and not args.html and not args.json:
        args.csv = True  # If no arguments are provided, default to CSV export

    if args.csv:
        df.to_csv("open-llm-leaderboard.csv", index=False)
        print("Data exported to CSV")

    if args.html:
        df.to_html("open-llm-leaderboard.html", index=False)
        print("Data exported to HTML")

    if args.json:
        df.to_json("open-llm-leaderboard.json", orient='records')
        print("Data exported to JSON")


if __name__ == "__main__":
    main()
