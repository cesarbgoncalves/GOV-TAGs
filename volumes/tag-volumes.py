import boto3
import time
from time import sleep
import json

ec2 = boto3.client('ec2')

volumes = {}
tags_list = []
vol_tag_fora_padrao = {}
volume_ok = 0
entrou_no_else = 0
tags_condition = ['Service', 'Environment', 'Country', 'Product', 'Platform', 'Owner']

for response in ec2.get_paginator('describe_volumes').paginate():
    volumes.update([(volume['VolumeId'], volume) for volume in response['Volumes']])
    for k, v in volumes.items():
        if volume_ok == 1:
            volume_ok = 0
            continue
        elif 'Tags' in v:
            for tag in v['Tags']:
                if tag["Key"] in tags_condition:
                    volume_ok += 1
                    if volume_ok >= 7:
                        volume_ok = 0
                        break
        else:
            print(k)