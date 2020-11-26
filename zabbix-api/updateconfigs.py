from pyzabbix.api import ZabbixAPI
import os

# URL do Zabbix
zabbix_url = 'https://zabbix.cloud.bionexo.com.br/'

# Coleta senha na memória do Computador
password = os.environ.get('PASS_ZABBIX')

# Coleta o usuario da memória do computador
username = os.environ.get('USER_ZABBIX')

# HostID e WebscenariosID
application_id = '378280'
host_id = '41880'

"""IDs dos hosts Biotracker no zabbix"""
# for host_id in range(41865, 41881):

# Autenticacao
zapi = ZabbixAPI(url=zabbix_url, user=username, password=password)


# For criado para alterar o intervalo de tempo
# de 1m para 5m
for host in range(41865, 41881):

    # Coleta Ids do Webscenarios a partir do HostID
    webscenarios_hosts = zapi.httptest.get(hostids=host)

    # Cria um lista de todos os Webscenarios (ID) do host informado acima
    https_ids = [i['httptestid'] for i in webscenarios_hosts]

    # Coleta todos os dados do Host a partir do Id informado no range do For
    dados_host = zapi.host.get(monitored_hosts=1, output='extend', hostids=host)

    # Pega apenas o nome do host nos dados coletados e cria uma lista
    nome_host = [i['name'] for i in dados_host]

    # Iterando na lista de Nome do Host
    for nome_do_host in nome_host:
        print(f'Alterando Web Scenarios do Host {host}')
        for web_id in https_ids:

            webscenario = zapi.httptest.update(httptestid=web_id, delay='5m')
            print(f'HostID: {host} -> HostName: {nome_do_host:<27} -> WebScenario: {web_id, webscenario}')


# Zabbix Logout
zapi.user.logout()
