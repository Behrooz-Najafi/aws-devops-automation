## Project Scenarios

### ✅ Scenario 1 – Manual S3 Upload
- Created a simple Python script (`backup_to_s3.py`)
- Manually uploaded a local file (`example.txt`) to an AWS S3 bucket using `boto3`

### 🔁 Scenario 2 – Daily Automated Backup
- Built an automated script (`daily_auto_backup.py`) that:
  - Creates/overwrites a local file (`example.txt`) with today’s date
  - Uploads the file to S3 daily (tested manually, ready for Windows Task Scheduler)

