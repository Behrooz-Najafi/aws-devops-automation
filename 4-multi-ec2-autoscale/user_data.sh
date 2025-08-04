#!/bin/bash
# ===== User Data Script for EC2 Auto Scaling Deployment =====

# 1. Update packages
yum update -y

# 2. Install Apache (httpd)
yum install -y httpd

# 3. Enable and start Apache service
systemctl enable httpd
systemctl start httpd

# 4. Install AWS CLI (for S3 access)
yum install -y awscli

# 5. Download website file from S3
aws s3 cp s3://elasticbeanstalk-us-east-2-582354273940/multi-ec2/index.html /var/www/html/index.html

# 6. Set proper permissions
chmod 644 /var/www/html/index.html

# 7. Restart Apache
systemctl restart httpd

