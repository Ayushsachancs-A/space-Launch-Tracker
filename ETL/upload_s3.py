import boto3
import os
from dotenv import load_dotenv

#load env
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET = os.getenv('BUCKET_NAME')

s3= boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = AWS_REGION

)

#function
def upload_file(file_path,key_path):
    try:
        s3.upload_file(file_path, S3_BUCKET, key_path)
        print("uploaded")
    except Exception as e:
        print(f"Error: {e}")

upload_file(r'C:\Users\imean\OneDrive\Desktop\projecttss\Space Launch Tracker\Data\clean_isro.csv','isro/clean_isro.csv')
upload_file(r'C:\Users\imean\OneDrive\Desktop\projecttss\Space Launch Tracker\Data\clean_spacex.csv','spacex/clean_spacex.csv')

