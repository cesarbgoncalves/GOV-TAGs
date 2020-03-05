import boto3

ec2 = boto3.client('ec2')

volumes = {}
tags_list = []
# tags_condition = ['Service', 'Environment', 'Country', 'Product', 'Platform', 'Owner']

for response in ec2.get_paginator('describe_volumes').paginate():
    volumes.update([(volume['VolumeId'], volume) for volume in response['Volumes']])
    for k, v in volumes.items():
        if 'Tags' in v:
            # print(f'Volume {v["VolumeId"]}, possui {len(v["Tags"])} TAGs')
            if v['Tags'] == 'Service' or \
                    v['Tags'] == 'Environment' or \
                    v['Tags'] == 'Country' or \
                    v['Tags'] == 'Product' or \
                    v['Tags'] == 'Platform' or \
                    v['Tags'] == 'Owner' or \
                    v['Tags'] == 'Name':
                pass
            else:
                print(v['VolumeId'])

            for tags in v['Tags']:
                print(tags['Key'])
            print('=' * 10)
        else:
            print(v["VolumeId"])
            print('=' * 10)
