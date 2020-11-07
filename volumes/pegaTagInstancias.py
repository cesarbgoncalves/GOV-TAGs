import boto3


def pega_nome_instancia(fid):
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Keys"] == 'Name':
            instancename = tags["Value"]
    return instancename


nomes = pega_nome_instancia()
print(nomes)
