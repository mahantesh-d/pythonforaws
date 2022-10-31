import boto3

s3 = boto3.client('s3',
                  aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXX',
                  aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

s3.download_file(Filename='logo.jpg', Bucket='mybotos3', Key='logo.jpg')
