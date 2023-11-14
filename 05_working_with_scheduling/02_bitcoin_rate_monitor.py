from rocketry import Rocketry
from rocketry.conds import cron

import csv, os, logging, requests

app = Rocketry()

def extract_bitcoin_rate():

    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    
    return response.json()

def transform_data(last_rate: dict):
    logging.warning("Transformando os dados da API bitcoin")

    updated_at =  last_rate['time']['updated']
    
    usd_rate = last_rate['bpi']['USD']['rate']
    gbp_rate = last_rate['bpi']['GBP']['rate']
    eur_rate = last_rate['bpi']['EUR']['rate']

    row = [
        { 'updated_at': updated_at, 'usd_rate': usd_rate, 'gbp_rate': gbp_rate, 'eur_rate': eur_rate }
    ]
    
    return row

def save_data(data: dict):
    file_path = './data/bitcoin_rate.csv'
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', encoding='UTF-8' ) as f:
        columns = [ 'updated_at', 'usd_rate', 'gbp_rate', 'eur_rate' ]

        writer = csv.DictWriter(f, fieldnames=columns)

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

    return True

@app.task(cron('* * * * *'))
def task():
    last_rate = extract_bitcoin_rate()

    last_rate_row = transform_data(last_rate)

    save_data(last_rate_row)

if __name__ == '__main__':
    app.run()





        