import os
import boto3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log(bucket_name,path,filename):
    try:
        client = boto3.client('s3')
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        cwd = os.getcwd()
        print(cwd)
        if os.path.isfile(path) :
            s3_key = f"{timestamp}_{filename}"
            client.upload_file(path,bucket_name,s3_key)
            print("File Uploaded succesfully")
        else:
            print("File not found in the mentioned directory")
    except Exception as error:
        print("Program Error: ", error)
    

def main():
    bucket_name = input( "Enter the bucket name: ").strip()
    path = input("Enter the local path for logs to share to s3: ").strip()
    filename = input("Enter the file name for s3 buckets: ").strip()
    log(bucket_name,path,filename)

if __name__ == "__main__":
    main()