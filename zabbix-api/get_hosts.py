from pyzabbix.api import ZabbixAPI
import os
from pprint import pprint

# URL do Zabbix
zabbix_url = 'https://zabbix.cloud.bionexo.com.br/'

# Coleta senha na memória do Computador
password = os.environ.get('PASS_ZABBIX')

# Coleta o usuario da memória do computador
username = os.environ.get('USER_ZABBIX')

# Autenticacao
zapi = ZabbixAPI(url=zabbix_url, user=username, password=password)

hosts = zapi.host.get(monitored_hosts=1, output='extend')

"""hostanames = [host['host'] for host in hosts]

for hostnames in hostanames:
    print(hostnames)

print(len(hostanames))"""

webscenarios_hosts = zapi.httptest.get(hostids='41865')
# webscenarios = zapi.httptest.get(hostids='41865', httptestids='348')

# for cenarios in webscenarios_hosts:
#     print(cenarios['httptestid'])

https_ids = [i['httptestid'] for i in webscenarios_hosts]


zapi.user.logout()
