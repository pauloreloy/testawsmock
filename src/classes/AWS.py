import boto3

class AWS:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def get_s3_object(self, bucket, key):
        response = self.s3_client.get_object(Bucket=bucket, Key=key)
        return response['Body'].read()