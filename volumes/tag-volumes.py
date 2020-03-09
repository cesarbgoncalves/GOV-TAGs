import boto3
import json
ec2 = boto3.client('ec2')
tags_condition = ['Environment', 'Country', 'Product', 'Platform', 'Owner']


def volumes_sem_tags():
    volumes = {}
    volumes_sem_tags = []
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
    return volumes_sem_tags


# volumes = {}
# for response in ec2.get_paginator('describe_volumes').paginate():
#     volumes.update([(volume['VolumeId'], volume) for volume in response['Volumes']])
#     print(volume['VolumeId'])

pag = ec2.get_paginator('describe_instances').paginate()

for page in pag:
    for res in page['Reservations']:
        for inst in res['Instances']:
            print(inst['InstanceId'])

# response = ec2.describe_instances()
# for i in response['Reservations']:
#     for t in i['Instances']:
#         if 'Tags' in t:
#             print(t)
#         else:
#             print(f'Não há TAGS na instância {t["InstanceId"]}')
