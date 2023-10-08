import pandas as pd
import requests, logging, json
from datetime import datetime as dt

# pd.read_json(): Ler dados de arquivos JSON

url = "https://world.openfoodfacts.net/api/v2/product/"
product = '7891000369371'

response = requests.request("GET", url + product)

if response.status_code == 200:
    logging.warning(f"Request succeeded with status code: { response.status_code }")

    data = response.json()
    status_code = data.get('status_verbose')
    if status_code == 'product found':
        
        # https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
        # normalize = transforma dados em formato JSON em um DataFrame
        product_info = data.get('product', None)
        df = pd.json_normalize(product_info)
        df['processed_at'] = dt.now().strftime('%Y-%m-%d %H:%M:%S') 

        # Salvando arquivo em formato JSON
        with open('./data/raw/json/product.json', 'w') as json_file:
            json.dump(df.to_dict(orient='records'), json_file, indent=2)
    else:
        logging.warning(f"status: {status_code}")
else:
    logging.warning(f"Request failed with status code: { response.status_code }")
