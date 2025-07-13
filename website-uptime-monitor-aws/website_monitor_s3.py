import requests
import boto3
import os
from datetime import datetime

# List of URLs to monitor
urls = [
    "https://github.com/Behrooz-najafi/aws-devops-automation",
    # "https://chatgpt.com/",
    # "https://gemini.google.com"
]

# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

# AWS Configs
sns = boto3.client("sns", region_name="us-east-2")
sns_topic_arn = "arn:aws:sns:us-east-2:582354273940:website-monitor-alerts"
s3 = boto3.client("s3")
bucket_name = "elasticbeanstalk-us-east-2-582354273940"

# Prepare log file path
base_path = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(base_path, "log.txt")

# Get timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Open log file and process URLs
with open(log_path, "a", encoding="utf-8") as logfile:
    for url in urls:
        try:
            response = requests.get(url, timeout=10, headers=headers)
            if response.status_code == 200:
                message = f"{timestamp} ✅ Site is UP: {url}\n"
            else:
                message = f"{timestamp} ⚠️ Site returned status {response.status_code}: {url}\n"
        except requests.exceptions.RequestException as e:
            message = f"{timestamp} ❌ Site is DOWN: {url} | Error: {e}\n"

        # Log and notify
        logfile.write(message)
        sns.publish(Subject="Website Status", Message=message, TopicArn=sns_topic_arn)
        print(message.strip())

# Upload the log to S3
s3.upload_file(log_path, bucket_name, "website-monitor/log.txt")
print("📤 Log uploaded to S3.")

