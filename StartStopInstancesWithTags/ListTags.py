import boto3

ec2 = boto3.resource('ec2')


# def lambda_handler(event, context):
def lambda_handler():
    running_with = []
    running_without = []

    for instance in ec2.instances.all():

        if instance.state['Name'] != 'running':
            continue

        has_tag = False
        for tag in instance.tags:
            if tag['Key'] == 'scheduleName' and tag['Value'] == '24x7':
                has_tag = True
                break

        if has_tag:
            running_with.append(instance.id)
        else:
            running_without.append(instance.id)

    #print("With: %s" % running_with)
    #print("Without: %s" % running_without)

    for instance in running_without:
        print(instance)


lambda_handler()
