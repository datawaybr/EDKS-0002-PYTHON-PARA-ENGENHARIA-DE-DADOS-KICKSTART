# pip install rocketry
# pip install psutil
# pydantic==1.10.10

from rocketry import Rocketry
from rocketry.conds import cron
from datetime import datetime as dt

import psutil
import csv
import os

import logging

app = Rocketry()

def get_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    return ram_usage

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

def transform_data(ram: float, cpu: float):
    logging.warning("Transforming data to list of dictionaries")

    updated_at = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    data = [
        { "updated_at": updated_at, "cpu": cpu, "ram": ram }
    ]

    return data

def save_data(data: dict):
    file_path = './data/cpu_stats.csv'
    file_exists = os.path.exists(file_path)

    logging.warning(f"Saving data into { file_path }")

    with open(file_path, 'a', encoding='UTF8', newline='') as f:
        field_names= ['updated_at', 'cpu', 'ram']

        writer = csv.DictWriter(f, fieldnames=field_names)

        if not file_exists:
            writer.writeheader()

        writer.writerows(data)

@app.task(cron('* * * * *'))
def task():
    
    ram = get_ram_usage()
    logging.warning(f"RAM usage: {ram}%")

    cpu = get_cpu_usage()
    logging.warning(f"CPU usage: {cpu}%")

    system_usage = transform_data(ram, cpu)

    save_data(system_usage)

if __name__ == "__main__":
    app.run()