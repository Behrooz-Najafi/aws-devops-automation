import boto3
import os
from datetime import datetime

# Step 1 – Prepare file path in the script directory
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "example.txt")

# Step 2 – Write today's date to the file
today = datetime.today().strftime('%d.%m.%Y')
with open(file_path, "w") as file:
    file.write(f"Sample backup file content {today}")

# Step 3 – Upload the file to S3
s3 = boto3.client('s3')
bucket_name = 'elasticbeanstalk-us-east-2-582354273940'
s3.upload_file(file_path, bucket_name, 'example.txt')

# Step 4 – Confirmation message
print("✅ Backup file created and uploaded to S3 successfully.")




