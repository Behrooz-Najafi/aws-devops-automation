import boto3
s3 = boto3.client('s3')
s3.upload_file('example.txt', 'elasticbeanstalk-us-east-2-582354273940', 'example.txt') 
