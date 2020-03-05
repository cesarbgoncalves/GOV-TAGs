import boto3

ec2 = boto3.client('ec2')

volumes = {}
tags_list = []
tags_condition = ['Service', 'Environment', 'Country', 'Product', 'Platform', 'Owner']

for response in ec2.get_paginator('describe_volumes').paginate():
    volumes.update([(volume['VolumeId'], volume) for volume in response['Volumes']])
    for k, v in volumes.items():
        if 'Tags' in v:
            # print(f' Volume {v["VolumeId"]}, possui {len(v["Tags"])} TAGs')
            for tags in v['Tags']:
                t = 0
                for validacao in tags_condition:
                    if validacao == tags_condition[t]:
                        t += 1

            # for i in v['Tags']:
        else:
            print(v["VolumeId"])
        #
        #         if i['Key'] == 'Service' or \
        #                 i['Key'] == 'Environment' or \
        #                 i['Key'] == 'Country' or \
        #                 i['Key'] == 'Product' or \
        #                 i['Key'] == 'Platform' or \
        #                 i['Key'] == 'Owner' or \
        #                 i['Key'] == 'Name' or \
        #                 i['Key'].startswith('aws:'):
        #             pass
        #         else:
        #             print(v["VolumeId"])