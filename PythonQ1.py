'''For the above mentioned Python Service we need the boto3 and awscli are installed as prerequisites in our machine.'''

'''Like here by using pip install <package-name>,'''
$ pip install boto3
‘’‘This boto3 is used for the code which is in python and through which we can access the aws services using this - AWS SDK’’’

$ pip install awscli
‘’’This awscli is the necessory library as a prerequisite tool, by this we can set up the configuration like access key and secret key details with it’’’

$ aws configure
‘’’Here we have to give the values of aws access_key, secret_key, region and format like json python etc’’’

$aws s3 ls             ‘’’-- to check the we are able to fetch aws ‘’’

'''Then we have to configure an environment for example ‘test’.'''
$ aws configure --profile test
$ aws s3 ls --profile test
'''These steps helps to fetch and conforms as we have the s3 storage bucket in ‘test’ profile in the account

Let’s get connect to the Account for uploading and downloading the file as per the requirement in the following.,'''

$ import boto3 

session = boto3.Session(profile_name="test", region_name="us-east-1")
s3 = session.client('s3')buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print bucket['CreationDate'].ctime(), bucket['Name']
    

'''For Download a file download_file() and upload a file we can use upload_file() APIs'''
import boto3
s3 = boto3.client('s3')
s3.download_file(Bucket='mytestbucket', Key='xyz.txt', Filename='./xyz.txt')

'''whereas upload a file.,'''

import botos3
s3 = boto3.client('s3')
s3.upload_file(Bucket='mybucket', Key='xyz.txt', Filename='./xyz.txt')

'''For deleting the file from the same.,'''
import botos3
s3 = boto3.client('s3')
s3.delete_file(Bucket='mybucket', Key='xyz.txt', Filename='./xyz.txt')


