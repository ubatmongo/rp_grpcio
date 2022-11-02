import sys
import os
import json
from google.cloud import storage
from google.oauth2 import service_account
from google.cloud.exceptions import NotFound
from google.cloud.exceptions import Forbidden


def download():

    home_dir = os.getenv("HOME", "~")
    gcp_sa_path = "Library/Caches/mms_bazel_telemetry/remote_cache_gcp_sa_key.json"
    gcp_credentials_string = "{}/{}".format(home_dir, gcp_sa_path)
    bucket_name = "mms-bazel-remote-cache-test"
    blob_name = "test.jar"
    local_file_name = "/Users/udita.bose/Documents/test.jar"

    print('Bucket:     ' + bucket_name)
    print('Object:     ' + blob_name)
    print('Local file: ' + local_file_name)

    print('Downloading an object from a Cloud Storage bucket to a local file ...')

    # Instantiate the client.
    with open(gcp_credentials_string, "r") as sa_json:
        gcp_json_credentials_dict = json.load(sa_json)
    if not gcp_json_credentials_dict:
        print("can not find sa json")
        sys.exit(1)

    credentials = service_account.Credentials.from_service_account_info(gcp_json_credentials_dict)
    client = storage.Client(project=gcp_json_credentials_dict['project_id'], credentials=credentials)

    try:
        # Get the bucket.
        bucket = client.get_bucket(bucket_name)
        # Instantiate the object.
        blob = bucket.blob(blob_name)
        # Downloads an object from the bucket.
        blob.download_to_filename(local_file_name)
        print('\nDownloaded')
    except NotFound:
        print('Error: Bucket/Blob does NOT exists!!')
        pass
    except Forbidden:
        print('Error: Forbidden, you do not have access to it!!')
        pass

    return
