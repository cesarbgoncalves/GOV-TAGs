from pyzabbix.api import ZabbixAPI
import csv

application_id = '378280'
host_id = '41880'

# URL do Zabbix
zabbix_url = 'https://zabbix.cloud.bionexo.com.br/'

# Coleta senha na memória do Computador
password = os.environ.get('PASS_ZABBIX')

# Coleta o usuario da memória do computador
username = os.environ.get('USER_ZABBIX')


"""IDs dos hosts no zabbix"""
# for host_id in range(41865, 41881):

count = 0

# Autenticacao
zapi = ZabbixAPI(url=zabbix_url, user=username, password=password)

arq = csv.reader(open('webservices.csv'))

for linha in arq:

    web_results = zapi.httptest.create(name=linha[1], hostid=host_id, authentication='0', retries='1',
                                       applicationid=application_id, steps=[{'url': linha[0], 'name': linha[1],
                                                                             'no': 1, 'status_codes': '200'}])

    count += 1
    print(f'{count:>2}º -> {web_results} -> {linha[2]}')


zapi.user.logout()
