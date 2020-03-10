import boto3
import json

ec2 = boto3.client('ec2')
ec2resource = boto3.resource('ec2')
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
    instancias = list(inst_com_volumes_sem_tags())
    for i in response['Reservations']:
        for t in i['Instances']:
            tag_instancia = t['InstanceId']
            for u in t['Tags']:
                if u['Key'] in tags_condition:
                    tag_k = u['Key']
                    tag_v = u['Value']
                    # print(u['Key'], u['Value'])
            print(tag_instancia)

def teste2():
    dict = {}
    volumes = ec2resource.volumes.all()
    for volume in volumes:
        for vol in volume.attachments:
            for key, value in dict.items():



teste2()






# import boto3
#
# client = boto3.client('ec2')
#
# custom_filter = [{
#     'Name':'tag:Owner',
#     'Values': ['user@example.com']}]
#
# response = client.describe_instances(Filters=custom_filter)







""" SCRIPT DE TESTE QUE PEGUEI.
# -----26/07/2019-----#
# --- Script for update the volume tags in which is not matching with instance tags---
# !/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')


# -----Define Lambda function-----#
def lambda_handler(event, context):
    # -----Check& filter Instances which  Kloud_managed equal true-----#
    instances = ec2client.describe_instances(Filters=[{'Name': 'tag:kloud_managed', 'Values': ['True']}])

    # -----Define dictionary to store Tag Key & value------#
    dict = {}

    # -----Store Key & Value of Instance Tag:“Name” ------#
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    # print ( instance['InstanceId'],tag['Value'])
                    # ids.append(( instance['InstanceId'],tag['Value']))
                    dict[instance['InstanceId']] = tag['Value']

    # -----Store Key & Value with attached instance ID of all volumes ------#     
    volumes = ec2.volumes.all()
    for volume in volumes:

        # -----compare dictionary value Key:InstanceID and volume attached Key:InstanceID ------#     
        for a in volume.attachments:
            for key, value in dict.items():

            # -----compare dictionary value Key:InstanceID and volume attached Key:InstanceID ------# 
            # -----If the InstanceID matched create new Tag:’Kloud_Name’ with key of value: servername ------#     

            if a['InstanceId'] == key:
                volume.create_tags(Tags=[{'Key': 'Kloud_Name', 'Value': value}])
                
"""