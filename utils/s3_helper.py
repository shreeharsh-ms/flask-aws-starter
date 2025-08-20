import boto3
import os

# Get values from environment (only region + bucket needed)
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")  
S3_BUCKET = os.getenv("S3_BUCKET", "flask-app-images-dev")


# Create S3 client – no keys needed, boto3 will use IAM role
s3_client = boto3.client("s3", region_name=AWS_REGION)

def upload_file_to_s3(file_obj, filename):
    """Upload file object to S3 without ACL"""
    s3_client.upload_fileobj(file_obj, S3_BUCKET, filename)
    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"

def list_files_in_s3():
    """List files from S3"""
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
    if "Contents" in response:
        return [f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{obj['Key']}" for obj in response["Contents"]]
    return []
