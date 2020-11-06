import boto3
import subprocess

ec2 = boto3.client('ec2')
tags_condition = ['Environment', 'Country', 'Product', 'Platform', 'Owner']


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
            for teste in value['Attachments']:
                if teste['VolumeId'] in volumes_sem_tags:
                    inst_vol_notag.append(teste['InstanceId'])
    # return volumes_sem_tags
    return inst_vol_notag


def teste():
    tag_k = 0
    tag_v = 0
    tag_instancia = 0
    response = ec2.describe_instances(InstanceIds=inst_com_volumes_sem_tags())
    for i in response['Reservations']:
        for t in i['Instances']:
            tag_instancia = t['InstanceId']
            for u in t['Tags']:
                if u['Key'] in tags_condition:
                    tag_k = u['Key']
                    tag_v = u['Value']
            return tag_instancia


with open('instancias_sem_tag.txt', 'w+') as arquivo:
    for i in inst_com_volumes_sem_tags():
        arquivo.write(i+'\n')

subprocess.call(['/bin/bash','taguearVolumesigualEC2.sh'])

for i in inst_com_volumes_sem_tags():
    print(i)
