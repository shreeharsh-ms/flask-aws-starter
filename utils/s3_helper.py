import boto3
from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_file_to_s3(file_obj, filename):
    """Upload file object to S3"""
    s3_client.upload_fileobj(file_obj, S3_BUCKET, filename, ExtraArgs={"ACL": "public-read"})
    return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{filename}"

def list_files_in_s3():
    """List files from S3"""
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
    if "Contents" in response:
        return [f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{obj['Key']}" for obj in response["Contents"]]
    return []
