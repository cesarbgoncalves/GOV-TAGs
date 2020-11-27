from pyzabbix.api import ZabbixAPI
import os


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

for host_id in 41879, 41872, 41880:

    application_create = zapi.application.create(name='Validacao_web', hostid=host_id)
    count += 1
    print(f'{count:>2}º -> {application_create}')


zapi.user.logout()
