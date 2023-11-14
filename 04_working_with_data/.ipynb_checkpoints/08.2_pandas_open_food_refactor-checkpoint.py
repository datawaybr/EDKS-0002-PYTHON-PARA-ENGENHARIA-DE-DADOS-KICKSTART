import pandas as pd
import requests, logging

from datetime import datetime as dt

def extract_data_from_api(product:str):
    url = "https://world.openfoodfacts.net/api/v2/product/"
    full_url = url + product

    response = requests.get(full_url)

    return response.json()


def add_custom_columns(df:pd.DataFrame):

    df['processed_at'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    df['proccesed_by'] = 'etl_process'
    df['last_modified_t'] = pd.to_datetime(df['last_modified_t'], unit='s')

    return df


def transform_data(data:dict):
    product_info = data.get('product', None)
    df = pd.json_normalize(product_info)
    
    df_select_cols = df[['code','product_name','image_front_url', 'last_modified_t']].copy()

    df_select_cols = add_custom_columns(df_select_cols)

    return df_select_cols


def save_csv(data:dict):
    data.to_csv('./data/raw/csv/product.csv', index=False)


if __name__ == '__main__':
    product = '7891000369371'
    
    response = extract_data_from_api(product)
    status_code = response.get('status_verbose')
    
    if status_code == 'product found':
        df = transform_data(response)

        try:
            save_csv(df)
            logging.warning(f"Successfully saved file: product.csv")
        except Exception as e:
            logging.warning(f"Failed to save file: product.csv")
            logging.warning(f"Error: {e}")
    else:
        logging.warning(f"status: {status_code}")