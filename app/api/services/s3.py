import os

import boto3
from botocore.client import Config
from flask_security import current_user


def generate_presigned_post(file_name, file_type):
    # Initialise the S3 client
    s3 = boto3.client('s3', config=Config(s3={'addressing_style': 'path'}))
    S3_BUCKET = os.environ.get('S3_BUCKET')

    return s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = "users/{}/{}".format(str(current_user.id), file_name),
        Fields = {"acl": "public-read", "Content-Type": file_type},
        ExpiresIn = 3600
    )


def delete_obj(file_path):
    # Initialise the S3 client
    s3 = boto3.resource("s3")
    S3_BUCKET = os.environ.get('S3_BUCKET')
    obj = s3.Object(S3_BUCKET, file_path)
    obj.delete()
