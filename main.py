import datetime
import time
from pathlib import Path
from netmiko import ConnectHandler
from config import commands, routers

for router_name, router_settings in routers.items():
    if router_name not in ('R2', 'R3'):
        continue
    sshCli = ConnectHandler(**router_settings)
    command = '/export'
    output = sshCli.send_command(command)
    print(output)
    time.sleep(3)
    sshCli.disconnect()

    current_dir = Path.cwd()

    # Получаем текущую дату и время
    current_time = datetime.datetime.now()

    # Форматируем строку с датой и временем
    formatted_time = current_time.strftime('%Y-%m-%d_%H-%M')

    # Используем имя роутера и отформатированное время в названии файла
    filename = f'{router_name}_{formatted_time}-mikrotik-backup-netmiko.txt'
    with open(f'{current_dir}/backups/{filename}', 'w') as file:
        file.write(output)

