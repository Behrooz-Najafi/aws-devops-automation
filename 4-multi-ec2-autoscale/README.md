# 🌐 Multi-EC2 Auto Scaling Deployment (ALB + ASG + S3 + CloudWatch)

This project implements a **Highly Available** and **Scalable** architecture on AWS that automatically deploys a web application across multiple EC2 instances using **Load Balancing** and **Auto Scaling**.

---

## ✅ Scenario – Multi-EC2 Deployment with Auto Scaling & Monitoring

Implemented:

- **Application Load Balancer (ALB)** to distribute traffic across EC2 instances.
- **Auto Scaling Group (ASG)** to dynamically add/remove instances based on CPU utilization.
- **Launch Template** with **User Data** for:
  - Installing Apache Web Server.
  - Downloading `index.html` from an **S3 bucket**.
- **CloudWatch Monitoring** for:
  - Triggering scale-out and scale-in based on CPU utilization.
- **Stress Test** executed via **AWS Systems Manager (SSM)** without SSH.
- Resources deployed across **multiple Availability Zones (AZs)** for High Availability.

---

### ✅ AWS Services Used
- **EC2** – Runs the web application.
- **Application Load Balancer (ALB)** – Distributes traffic across EC2 instances.
- **Auto Scaling Group (ASG)** – Automatically scales EC2 instances.
- **S3** – Stores the HTML file for the website.
- **CloudWatch** – Monitors performance and triggers scaling.
- **IAM Roles** – Grants access to S3 and SSM.
- **AWS Systems Manager (SSM)** – Runs commands on EC2 without SSH.

---

## 📂 Project Structure
```bash
4-multi-ec2-autoscale/
│
├── README.md                       # Complete project documentation
├── user_data.sh                    # Bootstrap script to install Apache and deploy index.html
├── index.html                      # Test web page
├── architecture-diagram.png        # Architecture diagram
└── screenshots/                    # Screenshot folder
    ├── Launch Templates.png
    ├── multi-ec2-asg-lb-public.png
    ├── Target Group-multi-ec2-tg-public.png
    ├── Security Groups-Launch wizard.png
    ├── EC2 after scale in.png
    ├── Automatically scales EC2 instances.png
    ├── CloudWatch Monitoring scale-out and scale-in.png
    ├── multi-ec2-autoscale-role.png

