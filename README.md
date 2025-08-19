Flask AWS Starter 🚀

A simple **Flask web app** integrated with **AWS services**.  
This project demonstrates how to upload images to **Amazon S3**, display them in a **gallery**, and prepare for integration with **CloudWatch**, **Lambda**, **API Gateway**, and **Elastic Load Balancer (ALB)**.

--------------------------------------------------------------------

**Features**
-- Upload images via Flask web interface  
-- Store and fetch files from **AWS S3**  
-- View uploaded files in a simple **gallery**  
-- Health check endpoint (`/health`)  
-- Clean, modular project structure  
-- Ready for future AWS integrations:
   -- **Lambda** (automatic thumbnail generation after S3 upload)  
   -- **CloudWatch** (logs & custom metrics)  
   -- **API Gateway** (serverless `/stats` endpoint)  
   -- **Elastic Load Balancer (ALB)** (scalable deployment)

--------------------------------------------------------------------

**Project Structure**
flask-aws-starter/
│── app.py                 -> Flask app entry  
│── requirements.txt       -> Dependencies  
│── config.py              -> AWS & app config  
│── utils/
│   └── s3_helper.py       -> Helper functions for S3  
│── templates/
│   ├── base.html          -> Base layout  
│   ├── upload.html        -> Upload form  
│   └── gallery.html       -> Image gallery  
│── static/
│   └── style.css          -> Basic styling  
│── .gitignore             -> Ignore venv, __pycache__, .env, etc.  
│── README.md              -> This documentation

--------------------------------------------------------------------

**Prerequisites**
-- Python 3.9+  
-- An AWS account with permissions for S3 (and later: Lambda, CloudWatch, ALB, API Gateway)  
-- AWS credentials (Access Key ID and Secret Access Key)

--------------------------------------------------------------------

**Quick Start**

1) **Clone the repository**
   git clone https://github.com/<your-username>/flask-aws-starter.git
   cd flask-aws-starter

2) **Create and activate a virtual environment**
   Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate

   Windows (PowerShell):
   python -m venv venv
   venv\Scripts\activate

3) **Install dependencies**
   pip install -r requirements.txt

4) **Configure AWS credentials and settings**
   Option A — Environment variables (recommended):
   Mac/Linux (bash/zsh):
   export AWS_ACCESS_KEY_ID=your_key
   export AWS_SECRET_ACCESS_KEY=your_secret
   export S3_BUCKET=your_bucket_name

   Windows (PowerShell):
   setx AWS_ACCESS_KEY_ID "your_key"
   setx AWS_SECRET_ACCESS_KEY "your_secret"
   setx S3_BUCKET "your_bucket_name"

   Option B — .env file (don’t commit this file):
   Create a file named .env with:
   AWS_ACCESS_KEY_ID=your_key
   AWS_SECRET_ACCESS_KEY=your_secret
   S3_BUCKET=your_bucket_name

5) **Run the app (development)**
   python app.py
   Open http://127.0.0.1:5000 in your browser.

--------------------------------------------------------------------

**Endpoints**
-- `/upload`  -> Upload images (stored in S3)  
-- `/gallery` -> View all uploaded images pulled from S3  
-- `/health`  -> Health check (for load balancer target group)

--------------------------------------------------------------------

**How It Works (Phase 1)**
-- User uploads an image in `/upload`  
-- Flask uses **boto3** to upload the image to **S3**  
-- `/gallery` lists image objects from S3 and renders them as `<img>` tags  
-- `/health` returns a simple JSON to support ALB health checks

--------------------------------------------------------------------

**Next Phases (Roadmap)**
-- **Lambda**: Configure an S3 event trigger to invoke a Lambda that generates a thumbnail and stores it in a `/thumbs/` prefix.  
-- **CloudWatch**:  
   -- Send Flask logs to CloudWatch Logs.  
   -- Publish a custom metric (e.g., `uploads_count`) on each successful upload.  
-- **ALB**: Deploy the Flask app on EC2 or ECS and place it behind an Application Load Balancer using `/health` for target group checks.  
-- **API Gateway**: Expose a serverless `/stats` endpoint backed by Lambda that queries CloudWatch for recent upload metrics.

--------------------------------------------------------------------

**Security Notes**
-- **Never** commit credentials or secrets to Git.  
-- Use IAM users/roles with the **least privilege** required (S3 PutObject/GetObject/ListBucket, etc.).  
-- Consider using **AWS IAM Roles** (EC2/ECS Task Roles) instead of static keys in production.  
-- Set S3 bucket policies carefully; prefer signed URLs or private buckets for real apps.

--------------------------------------------------------------------

**Troubleshooting**
-- If uploads fail:  
   -- Verify `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `S3_BUCKET`.  
   -- Ensure your IAM policy allows `s3:PutObject`, `s3:ListBucket`, and `s3:GetObject`.  
-- If gallery is empty:  
   -- Confirm files exist in the S3 bucket and your region is correct.  
-- If Flask can’t find credentials:  
   -- Reopen terminal after `setx` on Windows, or re-source your shell on Mac/Linux.

--------------------------------------------------------------------

**Tech Stack**
-- **Flask** (Python web framework)  
-- **boto3** (AWS SDK for Python)  
-- **Amazon S3** (object storage)  
-- (Future) **AWS Lambda**, **CloudWatch**, **API Gateway**, **ALB**

--------------------------------------------------------------------

**License**
-- This project is licensed under the **MIT License**.  
-- You are free to use, modify, and distribute it for personal or commercial projects.

--------------------------------------------------------------------

**Contributing**
-- Contributions are welcome!  
-- Fork the repo, create a feature branch, and open a pull request.  
-- For major changes, please open an issue to discuss the proposal first.

--------------------------------------------------------------------

**Author**
-- Starter template by: <your-name-or-handle>  
-- GitHub: https://github.com/<your-username>
