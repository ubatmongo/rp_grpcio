import os.path
import sys

from google.cloud import storage

if __name__ == "__main__":
    storage_client = storage.Client.from_service_account_json(
        os.path.expanduser(
            "~/Library/Caches/mms_bazel_telemetry/remote_cache_gcp_sa_key.json"
        )
    )
    with open(os.devnull, "w") as tmp_file:
        storage_client.download_blob_to_file(
            "gs://mms-bazel-remote-cache-test/cas/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            tmp_file,
            timeout=1,
            retry=None,
        )

    print("Done", file=sys.stderr)
