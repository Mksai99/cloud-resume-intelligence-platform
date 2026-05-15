import boto3
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

s3_client = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION")
)

BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


def upload_file_to_s3(file, filename):

    unique_filename = f"{uuid.uuid4()}-{filename}"

    s3_client.upload_fileobj(
        file,
        BUCKET_NAME,
        unique_filename
    )

    file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{unique_filename}"

    return file_url