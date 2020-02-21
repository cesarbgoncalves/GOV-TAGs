import boto3
import json

client = boto3.client('ec2')
response = client.describe_snapshots(OwnerIds=['self'])
list_all_ami = client.describe_images(Owners=['self'])
snap_sem_tags = dict()
total_snaps = list()
amis_tag = dict()

for index, snapshots in enumerate(response['Snapshots']):
    # print(f'Descrição do Snapshot: {snapshots["Description"]}')
    # print(f'Start Time: {snapshots["StartTime"]}')
    # print(f'ID: {snapshots["SnapshotId"]}')
    # print(f'Volume Base: {snapshots["VolumeId"]}')
    # print(f'Tamanho: {snapshots["VolumeSize"]}Gb')
    if 'Tags' in snapshots:
        for index_tags, v_tags in enumerate(snapshots['Tags']): #v_tags é dicionario
            print(f'{v_tags["Key"]:>35}:{v_tags["Value"]:>35}')
    else:
        snap_sem_tags['Nr'] = (index + 1)
        snap_sem_tags['ID'] = (snapshots['SnapshotId'])
        snap_sem_tags['Desc'] = (snapshots['Description'])
        total_snaps.append(snap_sem_tags.copy())

    print('=' * 71)

print('=' * 80)
print()
print(f'Total de Snapshots sem TAGS {len(total_snaps)}:')
print('#############################################')
#############################################
for valores in total_snaps:
    if 'ami' in valores['Desc']:
        ami = valores['Desc'].split(" ")
        ami = ami[4]
        print(f'O Snap: {valores["ID"]}, é baseado na Imagem: {ami}')

    else:
        pass
print('===================================================================')
for indice, imagens in enumerate(list_all_ami['Images']):
    img = str(imagens['ImageId'])
    if 'Tags' in imagens:
        print('==' * 45)
        print(imagens['ImageId'])
        for tags in imagens['Tags']:
            print(tags['Value'])


