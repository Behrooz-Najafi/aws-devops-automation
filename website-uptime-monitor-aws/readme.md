# 🌐 Website Uptime Monitor (AWS + Python)

This project monitors the availability of a list of websites and logs their status.

---

## ✅ Scenario 1 – Website Uptime Logging (Local)

Created a Python script `website_monitor_s3.py` that:

- Sends HTTP GET requests to a list of predefined websites.
- Logs the result (✅ UP, ❌ DOWN, or ⚠️ Non-200) along with a timestamp to a local `log.txt` file.

- Can be manually run or has been successfully scheduled via **Windows Task Scheduler** ✅

---

## ☁️ Scenario 2 – Cloud-Native Automation with AWS Lambda

A second script `website_monitor_lambda.py` is adapted for AWS Lambda and includes:

- 📤 Uploading log content to an **S3 bucket** (`elasticbeanstalk-us-east-2-582354273940`).
- 📣 Sending alert messages via **SNS** when a site is DOWN or returns an unexpected status.

AWS services configured:

- **S3** – Used to store the uptime log file in cloud storage.
- **SNS** – Sends email notifications for failed checks.
- **IAM Role** – Custom permissions attached to allow `PutObject` to S3 and `Publish` to SNS.
- **Lambda Execution Role** – Scoped least-privilege permissions added manually.
- **EventBridge Scheduler** – Triggers Lambda function **weekly** under the name `website-monitor-weekly-schedule`.

---

## 📁 Project Structure

```bash
website-uptime-monitor-aws/
│
├── website_monitor_s3.py           # Local version (uses log.txt + can run via Task Scheduler)
├── website_monitor_lambda.py       # AWS Lambda version (uses io.StringIO + boto3)
├── log.txt                         # Log file (used in local run only)
└── readme.md                       # This documentation

