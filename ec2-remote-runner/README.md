# 💻 EC2 Remote Runner (System Monitoring via SSM + Lambda)

This project remotely collects system resource usage (disk, memory, CPU) from an EC2 instance using AWS Systems Manager and automates reporting via Lambda.

---

## ✅ Scenario – Scheduled EC2 Monitoring via SSM & Lambda

Created a Python script `ec2_monitor_lambda.py` that:

- Executes Linux commands on an EC2 instance **without SSH**, using **SSM (AWS Systems Manager)**.
- Retrieves the output for:
  - Disk usage (`df -h`)
  - Memory usage (`free -m`)
  - CPU load (`uptime`)
- Uploads the results to a specified **S3 bucket** under the path `ec2-monitoring/ec2_status_report.txt`.
- Sends **SNS alerts** if critical disk usage (e.g. `"99%"` or `"100%"`) is detected in the report.

AWS services configured:

- **EC2** – Instance being monitored (with IAM role allowing SSM access).
- **SSM** – Used to run shell commands securely on EC2.
- **S3** – Stores the monitoring report in a structured path.
- **SNS** – Sends alert notifications on critical usage.
- **IAM Role** – Lambda role with permissions to invoke SSM, write to S3, and publish to SNS.
- **Lambda** – Executes the monitoring logic and handles automation.
- **EventBridge Scheduler** – Triggers Lambda weekly under the name `ec2-monitor-cpu-ram-disk-weekly-schedule`.

---

## 📁 Project Structure

```bash
ec2-remote-runner/
│
├── ec2_monitor_lambda.py       # Lambda function to run SSM commands and upload logs
└── readme.md                   # This documentation

