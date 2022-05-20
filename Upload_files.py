import boto3

s3_resource=boto3.client("s3")

s3_resource.upload_file(
    Filename="testimage23.png",
    Bucket="rslbucket23345241",
    Key="testimage23.png"
    )