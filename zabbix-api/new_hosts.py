from pyzabbix import ZabbixAPI
import csv

zapi = ZabbixAPI("https://zabbix.cloud.bionexo.com.br/")
zapi.login(user='cgoncalves', password='.1@Dm1n)!0192')

zapi = ZabbixAPI(url='https://zabbix.cloud.bionexo.com.br/', user='cgoncalves', password='.1@Dm1n)!0192')

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
