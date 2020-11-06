import boto3
import json

client = boto3.client('ec2')

response = client.describe_images(Owners=['self'])

print(json.dumps(response, indent=2))
