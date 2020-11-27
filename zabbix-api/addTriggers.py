from pyzabbix.api import ZabbixAPI
import os


# URL do Zabbix
zabbix_url = 'https://zabbix.cloud.bionexo.com.br/'
# Coleta senha na memória do Computador
password = os.environ.get('PASS_ZABBIX')
# Coleta o usuario da memória do computador
username = os.environ.get('USER_ZABBIX')
# Autenticacao
zapi = ZabbixAPI(url=zabbix_url, user=username, password=password)

with open('webscenariosName.txt', 'r') as doc_nomes:
    for linha in doc_nomes:
        linha = linha.strip()
    #     trigger_webscenarios = zapi.trigger.create(description=f'[VidaFertil - {linha}]',
    #                                                expression=f'{{Biotracker - VidaFertil:web.test.fail[{linha}].min(6m)}}<>0',
    #                                                priority=3)

        print(linha)
