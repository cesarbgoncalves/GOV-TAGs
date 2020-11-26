from pyzabbix.api import ZabbixAPI
import csv

"""IDs dos hosts no zabbix"""
# for host_id in range(41865, 41881):

count = 0

zapi = ZabbixAPI(url='https://zabbix.cloud.bionexo.com.br/', user='cgoncalves', password='.1@Dm1n)!0192')

for host_id in 41879, 41872, 41880:

    application_create = zapi.application.create(name='Validacao_web', hostid=host_id)
    count += 1
    print(f'{count:>2}º -> {application_create}')


zapi.user.logout()
