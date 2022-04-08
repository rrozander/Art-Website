import os
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
  bucket_name = os.environ.get('S3_BUCKET_NAME', 'jp-art-website')