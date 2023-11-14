from rocketry import Rocketry
from rocketry.conds import cron
from datetime import datetime as dt

import psutil, csv, os, logging

app = Rocketry()

def get_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

def transform_data(ram: float, cpu: float):
    logging.warning("Transformando os dados de CPU e RAM")

    updated_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    data = [
        { 'updated_at': updated_at, 'cpu': cpu , 'ram': ram }
    ]

    return data

def save_data(data: dict):
    file_path = './data/system_monitor.csv'
    file_exists = os.path.exists(file_path)

    with open(file_path, 'a', encoding='UTF-8' ) as f:
        columns = [ 'updated_at', 'cpu', 'ram' ]

        writer = csv.DictWriter(f, fieldnames=columns)

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

    return True

@app.task(cron('* * * * *'))
def task():
    ram = get_ram_usage()
    cpu = get_cpu_usage()

    system_usage = transform_data(ram, cpu)

    save_data(system_usage)

if __name__ == '__main__':
    app.run()





        