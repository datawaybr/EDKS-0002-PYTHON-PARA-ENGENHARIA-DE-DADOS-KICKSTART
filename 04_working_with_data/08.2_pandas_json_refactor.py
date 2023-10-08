import pandas as pd
import requests, logging, json

from datetime import datetime as dt

# pd.read_json(): Ler dados de arquivos JSON

def extract_data_from_api(product:str):
    url = "https://world.openfoodfacts.net/api/v2/product/"
    full_url = url + product

    response = requests.request("GET", full_url)

    return response.json()


def add_custom_columns(df:pd.DataFrame):

    df['processed_at'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    df['proccesed_by'] = 'etl_process'

    return df


def transform_data(data:dict):
    product_info = data.get('product', None)
    df = pd.json_normalize(product_info)
    
    df = add_custom_columns(df)

    return df


def load_json_file(data:dict):
    with open('./data/raw/json/product_refactor.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == '__main__':

    product = '7891000369371'
    response = extract_data_from_api(product)

    status_code = response.get('status_verbose')
    
    if status_code == 'product found':
        df = transform_data(response)

        try:
            load_json_file(df.to_dict(orient='records'))
            logging.warning(f"Successfully saved file: product_refactor.json")
        except Exception as e:
            logging.warning(f"Failed to save file: product_refactor.json")
            logging.warning(f"Error: {e}")
    else:
        logging.warning(f"status: {status_code}")