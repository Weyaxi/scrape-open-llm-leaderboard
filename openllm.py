import pandas as pd
from datasets import load_dataset

def get_datas():
    dataset = load_dataset("open-llm-leaderboard/contents", split="train").sort("Average ⬆️", reverse=True)
    return pd.DataFrame(dataset)
