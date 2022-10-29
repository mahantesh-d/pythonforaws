import boto3

s3 = boto3.client('s3',
                  aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                  aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

response = s3.list_objects(Bucket='mybotos3')
print(response["Contents"])

for obj in response["Contents"]:
    print(f' {obj["Key"]}')
