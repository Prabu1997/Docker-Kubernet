### Program to delete the object ######

import os
import boto3

def delete_object(bucket_name,object_key):
    try:
        client = boto3.client('s3')
        client.delete_object(Bucket=bucket_name,Key=object_key) # Capital B and K
        print("bucket Object is deleted")
    except Exception as error:
        print("system error: ", error)
def main():
    bucket_name = input("Enter the bucket_name: ")
    object_key = input("Enter the Object Key which you want to delete: ")
    delete_object(bucket_name,object_key)

if __name__ == "__main__":
    main()