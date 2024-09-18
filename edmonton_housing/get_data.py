import pandas as pd
import requests

def get_data(dataset_identifier, params = {}):
    'A function to retrieve data from the City of Edmonton open data portal'

    # base URL for edmonton city data
    url = f"https://data.edmonton.ca/resource/{dataset_identifier}.json"

    # make api request, returning in json form
    response = requests.get(url, params = params).json()

    # convert response to dataframe
    response_df = pd.DataFrame.from_records(response)

    return response_df
