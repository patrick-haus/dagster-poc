from dagster_gcp import BigQueryResource

import dagster as dg


@dg.asset
def read_from_bigquery(bigquery: BigQueryResource):
    with bigquery.get_client() as client:
        query_job = client.query("SELECT * FROM `data-sandbox-354716.alo_yoga_input.1p_input_haus_export` LIMIT 10")
        rows = query_job.result() 
        for r in rows:
            print(r)

defs = dg.Definitions(
    assets=[read_from_bigquery], resources={"bigquery": BigQueryResource(project="data-sandbox-354716")}
)