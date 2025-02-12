import pandas as pd
from dagster import Definitions, asset
from dagster_gcp.gcs import GCSResource

@asset
def write_to_gcs(gcs: GCSResource):
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": ["A", "B", "C"]})

    csv_data = df.to_csv(index=False)

    gcs_client = gcs.get_client()

    bucket = gcs_client.bucket("hausstaging_sftp")
    blob = bucket.blob("users/patrick-test/my_dataframe.csv")
    blob.upload_from_string(csv_data)


@asset
def read_from_gcs(gcs: GCSResource):
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": ["A", "B", "C"]})

    csv_data = df.to_csv(index=False)

    gcs_client = gcs.get_client()

    bucket = gcs_client.bucket("hausstaging_sftp")
    blob = bucket.blob("users/patrick-test/my_dataframe.csv")
    text = blob.download_as_text()
    print(text) # see console log

defs = Definitions(
    assets=[write_to_gcs, read_from_gcs],
    resources={"gcs": GCSResource(project="data-sandbox-354716")},
)