import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3 = boto3.client('s3',
                              aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXX',
                              aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXX')
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3 = boto3.client('s3',
                              aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXX',
                              aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXX')
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False

    return True


# create_bucket('mybotos3')

create_bucket('mybotos3', 'ap-south-1')
