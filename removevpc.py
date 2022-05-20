import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId = 'vpc-09224d7b1549d3c0a')
    
print(response)
