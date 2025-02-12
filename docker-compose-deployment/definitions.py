import dagster as dg

@dg.asset
def asset_1():
    return 1

## Tell Dagster about the assets that make up the pipeline by
## passing it to the Definitions object
## This allows Dagster to manage the assets' execution and dependencies
defs = dg.Definitions(assets=[asset_1],
)