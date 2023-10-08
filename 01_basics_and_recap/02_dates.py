# Importando o módulo datetime
import datetime

# Criando um date
date = datetime.date(2022, 10, 31)
print(f"data: {date}")

# Criando um datetime
datetime_obj = datetime.datetime(2022, 10, 31, 12, 30, 45)
print(f"datahora: {datetime_obj}")

# Buscando o date atual
current_date = datetime.date.today()
print(f"hoje: {current_date}")

# Buscando o datetime atual
current_time = datetime.datetime.now()
print(f"agora: {current_time}")

# Formatando o date como string

date_string = datetime.date.today()
print(f"tipo antes da conversão: {type(date_string)} e valor: {date_string}")
date_string = date_string.strftime('%Y-%m-%d')
print(f"tipo após a conversão: {type(date_string)} e valor: {date_string}")

datetime_string = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_string)

# Adicionar ou subtrair um período de um objeto date
print(f"data: {date}")
new_date = date + datetime.timedelta(days=7)
print(f"data mais 7 dias: {new_date}")

# Adicionar ou subtrair um período de um objeto datetime
print(f"datetime: {datetime_obj}")
new_datetime = datetime_obj - datetime.timedelta(hours=3)
print(f"datetime mais 3 horas: {new_datetime}")

# Comparar date ou datetimes
is_before_datetime = datetime_obj < current_time
print(f"datetime menor que agora: {is_before_datetime}")