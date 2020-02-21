"""
Script desenvolvido para listar TAGs dos Snapshots e ser reutilizado para qualquer outro fim, nesse sentido.
"""

""" Import """
import boto3
import json
from itertools import count

""" Variaveis """
amis_sem_tags = dict()
total_amis = list()
amis_tag = dict()
id_imagem = dict()

""" Instanciamento do servico ec2 para as variaveis """
client = boto3.client('ec2')
response = client.describe_images(Owners=['self'])

""" ======= INICIO DO FOR ======= """
for indice, imagens in enumerate(response['Images']):
    img = str(imagens['ImageId'])
    if 'Tags' in imagens:
        print('==' * 45)
        print(imagens['ImageId'])
        for tags in imagens['Tags']:
            if 'Environment' in tags['Key']:
                print('adicionando chave Environment')
                amis_tag['Environment'] = "Sem TAG"

            elif 'Country' in tags['Key']:
                print('adicionando chave Country')
                amis_tag['Country'] = "Sem TAG"

            elif 'Platform' in tags['Key']:
                print('adicionando chave Platform')
                amis_tag['Platform'] = "Sem TAG"

            elif 'Product' in tags['Key']:
                print('adicionando chave Product')
                amis_tag['Product'] = "Sem TAG"
            else:
                # 'Owner' in tags['Key']:
                print('adicionando chave Owner')
                amis_tag['Owner'] = "Sem TAG"
    else:
        amis_sem_tags['Nr'] = (indice+1)
        amis_sem_tags['ID'] = (imagens['ImageId'])
        amis_sem_tags['ImgLocate'] = (imagens['ImageLocation'])
        total_amis.append(amis_sem_tags.copy())
print(type(amis_tag))

# """  ======= FIM DO FOR ======= """



print('==' * 45)
print()
print(f'Total de AMIs sem TAGS {len(total_amis)}:')
for valores_ami in total_amis:
    print(f'{valores_ami["ID"]} -> {valores_ami["ImgLocate"]}')
