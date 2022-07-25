# This simple Python script will ask for a bucket name and 
# proceed to delete all versions of all objects in said bucket
# 
# Requires:
#   - python3
#   - boto3 - pip install boto3

#!/usr/bin/env python
import boto3

BUCKET = input("Enter the bucket name: ")

s3 = boto3.resource('s3')
bucket = s3.Bucket(BUCKET)
bucket.object_versions.delete()