import boto3

client=boto3.client("ec2")

#how to describe all VPCs in your account

client.describe_vpcs()
print(client.describe_vpcs())