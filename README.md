# 🚀 AWS DevOps Automation Projects

This repository contains a collection of practical DevOps and automation projects built using **AWS services** and **Python**.  
Each project is self-contained and demonstrates hands-on skills with cloud infrastructure, scripting, and automation workflows.

---

## 📦 Projects

### 1. [🔁 S3 Backup Tool](./s3-backup-tool)

A simple Python tool to automatically back up local directories to an Amazon S3 bucket.  
It supports versioning, error logging, and is suitable for scheduled local automation or future deployment on cloud.

**Highlights:**
- Uploads files to S3 with structured naming  
- Handles nested folders  
- Ready for automation with Windows Task Scheduler or Lambda (future plan)

---

### 2. [🌐 Website Uptime Monitor](./website-uptime-monitor-aws)

A monitoring tool that checks if websites are online and logs the results.  
Supports both **local execution** and **cloud-native automation via AWS Lambda** with weekly scheduling.

**Highlights:**
- Logs website status (UP/DOWN)  
- Sends SNS alerts for failures  
- Uploads logs to S3  
- Integrated with Lambda + EventBridge (runs every Monday)

---

### 3. [📊 EC2 Remote Runner (SSM + Lambda)](./ec2-remote-runner)

A server monitoring system that runs shell commands on an EC2 instance using AWS Systems Manager and stores the output in S3.  
Also includes an alert system via SNS for critical disk usage.

**Highlights:**
- Collects disk, memory, and CPU usage via `df`, `free`, and `uptime`
- Uses SSM to remotely run commands without SSH access
- Stores results in an S3 bucket in text format
- Sends SNS alerts for high disk usage (e.g., `99%`, `100%`)
- Scheduled to run weekly via EventBridge under the name:  
  `ec2-monitor-cpu-ram-disk-weekly-schedule`

---

## 🛠️ Tech Stack

- AWS S3, Lambda, SNS, EventBridge, SSM
- Python (boto3)
- Git + GitHub
- Windows Task Scheduler (for local automation)

---

## 📚 Future Plans

- Migrate automation to **Infrastructure as Code** using **Terraform**
- Add CloudWatch Alarms and custom dashboards
- Expand to multi-region AWS deployments

---

## 👤 Author

**Behrooz Najafi**  
📍 Toronto, Canada  
📧 najafi.behrooz@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/yourprofile) *(optional)*

---

Feel free to explore the folders above and run each project independently.

