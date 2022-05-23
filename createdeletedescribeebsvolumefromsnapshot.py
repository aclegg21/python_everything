#how to create aws ebs volume from snapshot using boto3 and python

import boto3

ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='string',
Encrypted=True,
Size=12,
SnapshotId='snap-xxxxxxxxxxx',
VolumeType='string')


#how to delete snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.delete_snapshot(SnapshotId='snap-xxxxxxxxxxx')

#how to describe snapshot

import boto3

ec2_client=boto3.client("ec2")

ec2_client.describe_snapshots(SnapshotIds=['snap-xxxxxxxxxx'])