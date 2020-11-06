import boto3

ec2 = boto3.client('ec2')
ec2_resource = boto3.resource('ec2')
tags_condition = ['Environment', 'Country', 'Product', 'Platform', 'Owner']
regionid = "us-east-1"
profile = "default"


def inst_com_volumes_sem_tags():
    volumes = {}
    volumes_sem_tags = []
    inst_vol_notag = []
    for response in ec2.get_paginator('describe_volumes').paginate():
        volumes.update([(volume['VolumeId'], volume) for volume in response['Volumes']])
        for vol_id, value in volumes.items():
            tags_ok = 0
            if 'Tags' in value:
                for tag in value['Tags']:
                    if tag["Key"] in tags_condition:
                        tags_ok += 1
                        if tags_ok == len(tags_condition):
                            break
                if tags_ok < len(tags_condition):
                    volumes_sem_tags.append(vol_id)
            else:
                volumes_sem_tags.append(vol_id)
            for vols in value['Attachments']:
                if vols['VolumeId'] in volumes_sem_tags:
                    inst_vol_notag.append(vols['InstanceId'])
    return inst_vol_notag


# Pega o ID de cada instância sem TAG
for instanceID in inst_com_volumes_sem_tags():
    print(instanceID)
    # Começa a validar cada TAG da instância coletada pelo def acima
    for tagMap in tags_condition:
        # Pega o valor das TAGs uma por vez.
        ec2instance = ec2_resource.Instance(instanceID)
        for tags in ec2instance.tags:
            if tags['Key'] == tagMap:
                tagData = tags['Key']
    for device in ec2instance.block_device_mappings:
        volume = device.get('Ebs')
        volumeID = volume.get('VolumeId')
        print(f'Volume coletado: {volumeID}')







# for i in inst_com_volumes_sem_tags():
#     print(i)





"""
Parei aqui, Nesse momento já consigo pegar a TAG de cada instância, bem como 
os IDs de seus volumes. Só falta associar as tags que forem coletadas à cada VolumeID
"""
