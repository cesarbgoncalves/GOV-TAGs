"""
Script desenvolvido para listar TAGs dos Snapshots e ser reutilizado para qualquer outro fim, nesse sentido.
"""
from typing import List, Any

""" Import """
import boto3
import json
from itertools import count
import time

""" Variaveis """
amis_sem_tags = dict()
total_amis = list()
amis_tag = dict()
id_imagem = dict()
img_sem_Environment = []
img_sem_Country = []
img_sem_Platform = []
img_sem_Product = []
img_sem_Owner = []

""" Instanciamento do servico ec2 para as variaveis """
client = boto3.client('ec2')
response = client.describe_images(Owners=['self'])

""" ======= INICIO DO FOR ======= """
for indice, imagens in enumerate(response['Images']):
    if 'Tags' in imagens:
        img_sem_Environment.append(imagens['ImageId'])
        img_sem_Country.append(imagens['ImageId'])
        img_sem_Platform.append(imagens['ImageId'])
        img_sem_Product.append(imagens['ImageId'])
        img_sem_Owner.append(imagens['ImageId'])
        for tags in imagens['Tags']:
            print(f'Verificando a TAG {tags["Key"]} da Imagem {imagens["ImageId"]}')
            # time.sleep(0.2)
            if 'Environment' == tags['Key']:
                img_sem_Environment.pop()

            elif 'Country' == tags['Key']:
                img_sem_Country.pop()

            elif 'Platform' == tags['Key']:
                img_sem_Platform.pop()

            elif 'Product' == tags['Key']:
                img_sem_Product.pop()

            elif 'Owner' == tags['Key']:
                img_sem_Owner.pop()
    else:
        amis_sem_tags['Nr'] = (indice + 1)
        amis_sem_tags['ID'] = (imagens['ImageId'])
        amis_sem_tags['ImgLocate'] = (imagens['ImageLocation'])
        total_amis.append(amis_sem_tags.copy())
    print('\033[31m=\033[m' * 30)

print(f'Imagens sem a TAG Environment: {img_sem_Environment}')
print(f'Imagens sem a TAG Country: {img_sem_Country}')
print(f'Imagens sem a TAG Platform: {img_sem_Platform}')
print(f'Imagens sem a TAG Product: {img_sem_Product}')
print(f'Imagens sem a TAG Owner: {img_sem_Owner}')

# """  ======= FIM DO FOR ======= """


print()
print(f'Total de AMIs sem TAGS {len(total_amis)}:')
for valores_ami in total_amis:
    print(f'{valores_ami["ID"]} -> {valores_ami["ImgLocate"]}')
