# import boto3
#
# client = boto3.client('networkmanager')
#
# response = client.describe_client_vpn_target_networks()
#
# for i in response:
#     print(response)


############################################################
import boto3
import json
from pprint import pprint

ec2 = boto3.client('ec2')

response = ec2.describe_vpn_connections()

# conexoes = response['VpnConnections'][1]['VgwTelemetry'][1]['Status']
qtd_conexoes = len(response['VpnConnections'])


for conexao in range(0, qtd_conexoes):
    vpn_name = response['VpnConnections'][conexao]['Tags'][5]['Value']
    vpn_conn_1 = response['VpnConnections'][conexao]['VgwTelemetry'][0]['Status']
    vpn_conn_2 = response['VpnConnections'][conexao]['VgwTelemetry'][1]['Status']
    print(f'VPN name: {vpn_name} \n Conexão 1 = {vpn_conn_1} \n Conexão 2 = {vpn_conn_2}')