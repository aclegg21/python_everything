import boto3

s3_resource=boto3.client("s3")

#delete single object
s3_resource.delete_object(Bucket='rslbucket23345241', Key='testimage23.png')

#delete multiple objects
import os
import glob

objects=s3_resource.list_objects(Bucket='rslbucket23345241')['Contents']

len(objects)

#iteration
for object in objects:
    response=s3_resource.delete_object(Bucket='rslbucket23345241', 
    Key=object["Key"])
    print(response)