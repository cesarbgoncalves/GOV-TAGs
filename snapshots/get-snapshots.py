import boto3
import json

client = boto3.client('ec2')
response = client.describe_snapshots(OwnerIds=['self'])
list_all_ami = client.describe_images(Owners=['self'])
snap_sem_tags = dict()
total_snaps = list()
amis_tag = dict()

for index, snapshots in enumerate(response['Snapshots']):
    if 'Tags' in snapshots:
        for tags in snapshots['Tags']:
            print(f'{tags["Key"]:>35}:{tags["Value"]:>35}')
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
