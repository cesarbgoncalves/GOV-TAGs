import boto3
client = boto3.client('ec2')
a = client.describe_instances()
y="Owner"
print(a)
# for i in a['Reservations']:
#    for j in i['Instances']:
#      for k in range(len(j['Tags'])):
#         if y == j['Tags'][k]['Key']:
#             print("The following Instance does not have Owner Tag: "+j['InstanceId'])