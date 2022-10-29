import boto3

s3 = boto3.client('s3',
                  aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXXX',
                  aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXX')

response = s3.upload_file('logo.jpg', 'mybotos3', 'logo.jpg')
print(response)
