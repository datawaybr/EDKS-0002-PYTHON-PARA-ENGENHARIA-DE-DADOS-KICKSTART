# pip install rocketry
# pip install requests
# pydantic==1.10.10

from rocketry import Rocketry
from rocketry.conds import cron

import csv, os, logging
import requests

app = Rocketry()

def extract_bitcoin_rate():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    
    return response.json()

def transform_data(last_price_request: dict):
    
    updated_at =  last_price_request['time']['updated']
    
    usd_rate = last_price_request['bpi']['USD']['rate']
    gbp_rate = last_price_request['bpi']['GBP']['rate']
    eur_rate = last_price_request['bpi']['EUR']['rate']

    row = [
        { 'updated_at': updated_at, 'usd_rate': usd_rate, 'gbp_rate': gbp_rate, 'eur_rate': eur_rate }
    ]

    return row

def save_data(data: dict):
    file_path = './data/bitcoin_index.csv'
    file_exists = os.path.exists(file_path)

    logging.warning(f'Saving data into { file_path }')

    with open(file_path, 'a', encoding='UTF8', newline='') as f:
        field_names= ['updated_at', 'usd_rate', 'gbp_rate', 'eur_rate' ]

        writer = csv.DictWriter(f, fieldnames=field_names, delimiter=';')

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

@app.task(cron('* * * * *'))
def task():
    
    last_price_request = extract_bitcoin_rate()

    last_price = transform_data(last_price_request)

    save_data(last_price)

if __name__ == '__main__':
    app.run()