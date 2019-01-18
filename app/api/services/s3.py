import os

import boto3


def generate_presigned_post(file_name, file_type):
    # Initialise the S3 client
    s3 = boto3.client('s3')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    return s3.generate_presigned_post(
        Bucket = S3_BUCKET,
        Key = file_name,
        Fields = {"acl": "public-read", "Content-Type": file_type},
        Conditions = [
            {"acl": "public-read"},
            {"Content-Type": file_type}
        ],
        ExpiresIn = 3600
    )
