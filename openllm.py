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
                    columns = data['components'][component_index]['props']['headers']
                    try:
                        results_json = {"T": results[0], "Model": results[-1]}

                        if len(columns) < 15: # If there are less than 15 columns (this number can definetly change), we know that we are trying wrong component index, so breaking loop to try next component index.
                            break

                        for col_index, col_name in enumerate(columns[2:-1], start=2):
                            results_json[col_name] = results[col_index]
                            
                    except IndexError:  # Wrong component index, so breaking loop to try next component index. (NOTE: More than one component index can give you some results but we must find the right component index to get all results we want.)
                        break
                    result_list.append(results_json)
                    i += 1
                except IndexError:  # No rows to extract so return the list (We know it is the right component index because we didn't break out of loop on the other exception.)
                    return result_list
        except (KeyError, TypeError):
            continue

    return result_list
