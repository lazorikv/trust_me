import json
import boto3
from botocore.client import Config


class AwsBucketApi:

    def __init__(self, bucket_name=None):
        settings = self.get_settings()
        self.bucket_name = bucket_name or settings.get("bucket_name")
        self.bucket = boto3.client("s3",
                                   aws_access_key_id=settings.get("user_access_id"),
                                   aws_secret_access_key=settings.get("user_secret"),
                                   region_name=settings.get("bucket_region"),
                                   config=Config(signature_version='s3v4', s3={"addressing_style": "path"})
                                   )

    def get_settings(self):
        with open("settings.json") as f:
            return json.load(f)

    def upload_file_to_s3(self, file, acl="public-read"):

        try:
            self.bucket.upload_fileobj(
                file,
                self.bucket_name,
                file.filename,
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type
                }
            )

        except Exception as e:
            # This is a catch all exception, edit this part to fit your needs.
            print("Something Happened: ", e)
            return e

        # after upload file to s3 bucket, return filename of the uploaded file
        return file.filename

    def delete_file(self, key):

        return self.bucket.delete_object(Bucket=self.bucket_name, Key=key)

    def delete_folder(self, prefix):
        params = {
            "Bucket": self.bucket_name,
            "Prefix": prefix
        }
        obj = self.bucket.list_objects(**params)
        for i in obj['Contents']:
            filename = i["Key"]
            self.delete_file(filename)
