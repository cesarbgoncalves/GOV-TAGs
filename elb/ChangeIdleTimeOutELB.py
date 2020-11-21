import boto3

client = boto3.client('elb')
elb_timeout = 150


def get_names_elb():
    response_name = client.describe_load_balancers()
    nomes = []
    for elb_name in response_name['LoadBalancerDescriptions']:
        nomes.append(elb_name['LoadBalancerName'])
    return nomes


def get_tags(elb):
    desc_tags = client.describe_tags(LoadBalancerNames=[elb])
    tags = desc_tags['TagDescriptions'][0]['Tags']
    return tags


def set_timeout_elb(timeout):
    response_describe = client.modify_load_balancer_attributes(
        LoadBalancerName=elbs,
        LoadBalancerAttributes={'ConnectionSettings': {'IdleTimeout': timeout}}
    )
    elb_name = response_describe['LoadBalancerName']
    timeout_elb = response_describe['LoadBalancerAttributes']['ConnectionSettings']['IdleTimeout']
    print(f"Nome do ELB: {elb_name} - Timeout: {timeout_elb}")


for elbs in get_names_elb():
    for tags in get_tags(elbs):
        if (tags['Key'] == 'Owner') and (tags['Value'] == 'regene'):
            set_timeout_elb(elb_timeout)