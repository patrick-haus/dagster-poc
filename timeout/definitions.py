import pandas as pd
import dagster as dg
import time

@dg.asset
def asset_1():
    time.sleep(60)
    return 1

my_job = dg.define_asset_job(
    name="my_job", selection="*", tags={"dagster/max_runtime": 1}
)

## Tell Dagster about the assets that make up the pipeline by
## passing it to the Definitions object
## This allows Dagster to manage the assets' execution and dependencies
defs = dg.Definitions(assets=[asset_1],
                      jobs=[my_job],
)