# coding: utf-8
import boto3
session = boto3.Session(profile_name='solvimm')
#s3 = session.resource(s3)
s3 = session.resource('s3')
#for bucket in s3.buckets.all():
 #   print(bucket)
    
#new_bucket = s3.create_bucket(Bucket='boto3-jvsb-lab')
#ec2_client = session.client('ec2')
#get_ipython().run_line_magic('history', '')
