import argparse
import requests
from bs4 import BeautifulSoupn
import pandas as pd


def get_json_format_data():
    url = 'https://huggingfaceh4-open-llm-leaderboard.hf.space/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    script_elements = soup.find_all('script')
    json_format_data = json.loads(str(script_elements[1])[31:-10])
    return json_format_data


def get_datas(data):
    for component_index in range(10, 50, 1): # component_index sometimes changes when they update the space, we can use this "for" loop to avoid changing component index manually
        try:
            result_list = []
            i = 0
            flag = True
            while True and flag:
                try:
                    results = data['components'][component_index]['props']['value']['data'][i][2:15]
                    type_of = data['components'][component_index]['props']['value']['data'][i][0]

                    try:
                        results_json = {"Type": type_of, "Model": results[-1], "Average": results[0], "ARC": results[1], "HellaSwag": results[2], "TruthfulQA": results[3], "Precision": results[6], "Hub License": results[7], "#Params (B)": results[8],  "Model Sha": results[11]}
                    except IndexError:
                        flag = False
                        continue

                    result_list.append(results_json)
                    i += 1
                except (IndexError, AttributeError):
                    return result_list
        except (KeyError, TypeError):
            continue

    return result_list


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
