from google.cloud import storage
import os

def upload_to_gcs(bucket_name, source_file, destination_blob):
    # Authenticate using the service account key
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "GCP_SERVICE_ACCOUNT_KEY"  # Replace with your service account key file

    # Initialize Google Cloud Storage client
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob)

    # Upload file
    blob.upload_from_filename(source_file)
    print(f"File {source_file} uploaded to {destination_blob} in bucket {bucket_name}.")

if __name__ == "__main__":
    bucket_name = "testingslack"  # Replace with your GCS bucket name
    source_file = "output_data.xlsx"
    destination_blob = "data/output_data.xlsx"

    upload_to_gcs(bucket_name, source_file, destination_blob)
