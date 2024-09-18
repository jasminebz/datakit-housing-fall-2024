import pandas as pd
from sodapy import Socrata

def get_data(dataset_identifier, token = None, limit = 2000):
    'A function to retrieve data from the City of Edmonton open data portal'

    # Unauthenticated client only works with public data sets. Note 'None'
    # in place of application token:
    client = Socrata("data.edmonton.ca", app_token=token)

    # results returned as JSON from API / converted to Python list of
    # dictionaries by sodapy.
    results = client.get(dataset_identifier, limit=limit)

    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)

    return results_df
