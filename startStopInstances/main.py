import boto3
import logging

# Configurando log
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Para testes em ambientes locais - Desabilitar em prod
boto3.setup_default_session(profile_name='dev')

# instanciando os recursos do tipo ec2
ec2 = boto3.resource('ec2')

tag_name = 'ScheduleStartStop'
tag_value = 'after10pm'

# def lambda_handler(event, context):
def lambda_handler():
    # Pegando Instancias com status Running e com a TAG específica
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        },
        {
            'Name': 'tag:tag_name',
            'Values': ['tag_value']
        }
    ]

    # filter the instances
    # ec2 = boto3.client('ec2', region_name=region)
    instances = ec2.instances.filter(Filters=filters)

    # locate all running instances
    instances_with_tag = [instance.id for instance in instances]

    # print the instances for logging purposes
    if instances_with_tag == '':
        print(instances_with_tag)

    # make sure there are actually instances to shut down.
    if len(instances_with_tag) > 0:
        # perform the shutdown
        shuttingdown = ec2.instances.filter(InstanceIds=instances_with_tag).stop()
        print(f'Desligando a instância: {instances_with_tag}')
    else:
        print("\n Nothing to see here")


if __name__ == '__main__':
    lambda_handler()
