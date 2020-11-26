from pyzabbix import ZabbixAPI
import csv

# URL do Zabbix
zabbix_url = 'https://zabbix.cloud.bionexo.com.br/'

# Coleta senha na memória do Computador
password = os.environ.get('PASS_ZABBIX')

# Coleta o usuario da memória do computador
username = os.environ.get('USER_ZABBIX')

# Autenticacao
zapi = ZabbixAPI(url=zabbix_url, user=username, password=password)

f = csv.reader(open('hosts.csv'))

for [hostname] in f:
    hostcriado = zapi.host.create(
        host=hostname,
        status=1,
        interfaces=[{
            "type": 1,
            "main": "1",
            "useip": 1,
            "ip": '127.0.0.1',
            "dns": "",
            "port": 10050
        }],
        groups=[{
            "groupid": 110
        }]  # ,
        # templates=[{
        #     "templateid": 10001
        # }]
    )
    print(f'{hostname} Criado com sucesso!')
