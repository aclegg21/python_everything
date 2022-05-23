import boto3

client = boto3.client('dynamodb', region_name='us-east-1')

response = client.scan(TableName='week15_project')

print(response)
