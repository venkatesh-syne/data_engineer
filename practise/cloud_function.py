import json
import os
import pandas as pd

from google.cloud import storage

def get_columns(schemas_blob, ds_name):
    schemas = json.loads(schemas_blob.download_as_string())
    column_details = sorted(schemas[ds_name], key=lambda col: col['column_position'])
    columns = list(map(lambda td: td['column_name'], column_details))
    return columns


def main(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    tgt_bucket_name = os.environ.get('TGT_BUCKET_NAME')
    schemas_file_path = os.environ.get('SCHEMAS_FILE_PATH')
    src_bucket_name = event['bucket']
    blob_name = event['name']
    print(f'Processing file {blob_name} in bucket {src_bucket_name}')
    gsclient = storage.Client()
    src_bucket = gsclient.get_bucket(src_bucket_name)
    schemas_blob = src_bucket.get_blob(schemas_file_path)
    ds_name = blob_name.split('/')[-2]
    columns = get_columns(schemas_blob, ds_name)
    df = pd.read_csv(f'gs://{src_bucket_name}/{blob_name}', names=columns)
    df.to_parquet(f'gs://{tgt_bucket_name}/{blob_name}.snappy.parquet')