import boto3

s3 = boto3.resource('s3')

data = open('logo.jpg', 'rb')

s3.Bucket('demos3-mys3bucket-7w5900qpjbg1').put_object(Key='logo.jpg', Body=data)