from pyzabbix.api import ZabbixAPI
from pprint import pprint

zapi = ZabbixAPI(url='https://zabbix.cloud.bionexo.com.br/', user='cgoncalves', password='.1@Dm1n)!0192')

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
