import boto3
import os
from dotenv import load_dotenv

load_dotenv()

comprehend = boto3.client(
    "comprehend",
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
)


def detect_entities(text):

    response = comprehend.detect_entities(
        Text=text[:5000],
        LanguageCode="en"
    )

    return response["Entities"]