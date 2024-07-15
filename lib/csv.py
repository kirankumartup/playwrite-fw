import os
import pandas as pd


def read_user_data(file_name: str):
    file_path = os.path.join('test_data', file_name)
    user_data = pd.read_csv(file_path)
    return user_data.to_dict(orient='records')
