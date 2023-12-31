import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def get_json_format_data():
    url = 'https://huggingfaceh4-open-llm-leaderboard.hf.space/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    script_elements = soup.find_all('script')
    json_format_data = json.loads(str(script_elements[1])[31:-10])
    return json_format_data


def get_datas(data):
    for component_index in range(10, 50, 1):  # component_index sometimes changes when they update the space, we can use this "for" loop to avoid changing component index manually
        try:
            result_list = []
            i = 0
            while True:
                try:
                    results = data['components'][component_index]['props']['value']['data'][i]
                    type_of_emoji = data['components'][component_index]['props']['value']['data'][i][0]

                    try:
                        results_json = {"T": type_of_emoji, "Model": results[-1], "Average ⬆️": results[2], "ARC": results[3], "HellaSwag": results[4], "MMLU": results[5], "TruthfulQA": results[6], "Winogrande": results[7], "GSM8K": results[8], "Type": results[9], "Architecture": results[10], "Precision": results[11], "Merged": results[12], "Hub License": results[13], "#Params (B)": results[14], "Hub ❤️": results[15], "Available on the Hub": results[16], "Model Sha": results[17], "Flagged": results[18]}
                    except IndexError:  # Wrong component index, so breaking loop to try next component index. (NOTE: More than one component index can give you some results but we must find the right component index to get all results we want.)
                        break
                    result_list.append(results_json)
                    i += 1
                except IndexError:  # No rows to extract so return the list (We know it is the right component index because we didn't break out of loop on the other exception.)
                    return result_list
        except (KeyError, TypeError):
            continue

    return result_list
