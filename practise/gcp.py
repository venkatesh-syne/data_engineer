from google.cloud import bigquery

# Define BigQuery client
client = bigquery.Client()

# Set the dataset and table where you want to load the data
dataset_id = 'your_project_id.your_dataset_id'
table_id = f'{dataset_id}.your_table_id'

# Path to your JSON file
json_file_path = 'path_to_your_file.json'

# Define the BigQuery schema (optional, if you don't specify schema BigQuery will infer it)
schema = [
    bigquery.SchemaField("id", "INTEGER"),
    bigquery.SchemaField("name", "STRING"),
    bigquery.SchemaField("address", "STRING")
]

# Load the JSON data into BigQuery
with open(json_file_path, 'rb') as json_file:
    job = client.load_table_from_file(
        json_file,
        table_id,
        job_config=bigquery.LoadJobConfig(
            schema=schema,  # Optional: Define schema if needed
            source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON  # Specify the format as JSON
        )
    )

# Wait for the job to complete
job.result()

# Verify the upload
print(f"Loaded {job.output_rows} rows into {table_id}.")
