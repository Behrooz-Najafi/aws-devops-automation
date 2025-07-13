✅ Scenario 1 – Website Uptime Logging
Created a Python script (website_monitor_s3.py) that:

Sends HTTP requests to a list of predefined websites

Logs the result (UP, DOWN, or status code) with a timestamp to a local file (log.txt)

☁️ Scenario 2 – AWS Integration
Integrated AWS services using boto3:

SNS: Sends alert emails when a site is down or returns non-200 status

S3: Uploads log.txt to an S3 bucket after every execution

⏱️ Scenario 3 – Automation Ready
The script is ready to be scheduled via:

Windows Task Scheduler for periodic execution

Or AWS Lambda (if ported slightly) for cloud-native automation
