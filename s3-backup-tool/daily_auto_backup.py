import boto3
from datetime import datetime

# Step 1 – Write today's date to the file
today = datetime.today().strftime('%d.%m.%Y')
with open("example.txt", "w") as file:
    file.write(f"Sample backup file content {today}")

# Step 2 – Upload the file to S3
s3 = boto3.client('s3')
bucket_name = 'elasticbeanstalk-us-east-2-582354273940'   
s3.upload_file('example.txt', bucket_name, 'example.txt')


