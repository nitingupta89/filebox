import os


def get_s3_url(file_name):
    # Load necessary information into the application
    S3_BUCKET = os.environ.get('S3_BUCKET')

    return 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
