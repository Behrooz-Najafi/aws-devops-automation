import boto3
import urllib.request
import io
from datetime import datetime

# List of websites to monitor
urls = [
    "https://github.com/Behrooz-najafi/aws-devops-automation",
    "https://chatgpt.com/",
    "https://gemini.google.com"
]

# Configure SNS for alerting
sns = boto3.client("sns", region_name="us-east-2")
sns_topic_arn = "arn:aws:sns:us-east-2:582354273940:website-monitor-alerts"

# Configure S3 for log upload
s3 = boto3.client("s3")
bucket_name = "elasticbeanstalk-us-east-2-582354273940"
s3_key = "website-monitor/log.txt"

# Main handler function for AWS Lambda
def lambda_handler(event, context):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create in-memory log file
    log_output = io.StringIO()

    for url in urls:
        try:
            # Create HTTP request with browser-like headers
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            response = urllib.request.urlopen(req, timeout=4)  
            status = response.getcode()
            
            if status == 200:
                message = f"{timestamp} ✅ Site is UP: {url}\n"
            else:
                message = f"{timestamp} ⚠️ Site returned status {status}: {url}\n"
        
        except Exception as e:
            message = f"{timestamp} ❌ Site is DOWN: {url} | Error: {e}\n"
            sns.publish(Subject="Website DOWN Alert", Message=message, TopicArn=sns_topic_arn)
        
        # Write result to virtual file
        log_output.write(message)
        print(message.strip())
    # Reset cursor before upload
    log_output.seek(0)
    s3.upload_fileobj(io.BytesIO(log_output.getvalue().encode()), bucket_name, s3_key)
    print("📤 Log uploaded to S3.")



