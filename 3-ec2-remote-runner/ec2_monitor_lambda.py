import boto3
import time
import json
import io
from datetime import datetime

# === Configuration ===
instance_id = 'i-0943fb9d936830d47'
bucket_name = 'elasticbeanstalk-us-east-2-582354273940'
s3_key = 'ec2-monitoring/ec2_status_report.txt'
sns_topic_arn = 'arn:aws:sns:us-east-2:582354273940:website-monitor-alerts'

# === AWS clients ===
ssm = boto3.client('ssm')
s3 = boto3.client('s3')
sns = boto3.client('sns')

# === Shell commands to collect system metrics ===
commands = [
    "echo '--- Disk Usage ---'",
    "df -h",
    "echo '--- Memory Usage ---'",
    "free -m",
    "echo '--- CPU Load ---'",
    "uptime"
]

def lambda_handler(event, context):
    # Send shell commands to EC2 instance via SSM
    response = ssm.send_command(
        InstanceIds=[instance_id],
        DocumentName="AWS-RunShellScript",
        Parameters={'commands': commands},
    )

    command_id = response['Command']['CommandId']

    # Wait for command to execute
    time.sleep(3)

    # Get command output
    output = ssm.get_command_invocation(CommandId=command_id, InstanceId=instance_id)
    result = output['StandardOutputContent']
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    full_report = f"[{timestamp}]\n{result}"

    # Upload report to S3
    s3.upload_fileobj(io.BytesIO(full_report.encode()), bucket_name, s3_key)

    # Send SNS alert only if high disk usage is detected (based on simple "99%" or "100%" match)
    if "100%" in result or "99%" in result:
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject="🚨 EC2 Resource Alert",
            Message=f"High resource usage detected on EC2 instance.\n\n{full_report[:500]}..."
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Monitoring completed and log uploaded.')
    }


