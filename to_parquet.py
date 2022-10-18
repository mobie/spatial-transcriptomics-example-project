import json
import os
import pandas as pd


def to_parquet():
    ds_folder = "./data/pos42"
    metadata_file = os.path.join(ds_folder, "dataset.json")
    with open(metadata_file) as f:
        metadata = json.load(f)
    sources = metadata["sources"]

    new_sources = {}
    for source_name, source in sources.items():
        source_type, source_data = next(iter(source.items()))
        if source_type == "spots":
            table_folder = os.path.join(ds_folder, source_data["tableData"]["tsv"]["relativePath"])
            table_path = os.path.join(table_folder, "default.tsv")
            table = pd.read_csv(table_path, sep="\t")

            parquet_path = os.path.join(table_folder, "default.parquet")
            table.to_parquet(parquet_path, index=False)
            source_data["tableData"]["parquet"] = {"relativePath": table_folder}

            source = {source_type: source_data}

        new_sources[source_name] = source

    metadata["sources"] = sources
    with open(metadata_file, "w") as f:
        json.dump(metadata, f)


to_parquet()
