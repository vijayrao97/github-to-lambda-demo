import pandas as pd
import requests
import json


def lambda_handler(event, context):
    # TODO implement
    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)

    d = {'col1': [1,2], 'col2': [3,4]}
    df = pd.DataFrame(data=d)
    print(df)
    print('Demo Completed !!!')

