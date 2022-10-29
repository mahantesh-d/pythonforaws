import boto3

s3 = boto3.client('s3',
                  aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXX',
                  aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXX')
response = s3.list_buckets()
print(response['Buckets'])

for bucket in response['Buckets']:
    print(f' {bucket["Name"]}')

