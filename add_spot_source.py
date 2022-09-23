import os
import mobie
import pandas as pd


def add_spot_source():
    ds_folder = "./data/pos42-spatial-transcriptomics"

    table_folder = os.path.join(ds_folder, "tables", "transcriptome")
    os.makedirs(table_folder, exist_ok=True)
    table_path = os.path.join(table_folder, "default.tsv")

    input_table = "/home/pape/Downloads/segmentedData-Tim-102219-Pos42-1error-sqrt6-2020-05-22.csv"
    table = pd.read_csv(input_table)

    table["spot_id"] = list(range(1, len(table) + 1))
    table.to_csv(table_path, index=False, sep="\t")

    metadata = mobie.metadata.read_dataset_metadata(ds_folder)
    metadata["sources"]["transcriptome"] = {
        "spots": {"tableData": {"tsv": {"relativePath": "tables/transcriptome"}}}
    }
    mobie.metadata.write_dataset_metadata(ds_folder, metadata)


def add_spot_display():
    ds_folder = "./data/pos42-spatial-transcriptomics"

    spot_view = {
        "uiSelectionGroup": "spots",
        "isExclusive": False,
        "sourceDisplays": [
            {
                "spotDisplay": {
                    "sources": ["transcriptome"],
                    "tables": ["default.tsv"]
                }
            }
        ]
    }

    metadata = mobie.metadata.read_dataset_metadata(ds_folder)
    metadata["views"]["transcriptome"] = spot_view
    mobie.metadata.write_dataset_metadata(ds_folder, metadata)


# add_spot_source()
add_spot_display()
