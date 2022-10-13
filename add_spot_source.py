import os
import mobie
import pandas as pd


def add_spot_source(name, point_fraction=None, shuffle=False):
    ds_folder = "./data/pos42"

    table_folder = os.path.join(ds_folder, "tables", name)
    os.makedirs(table_folder, exist_ok=True)
    table_path = os.path.join(table_folder, "default.tsv")

    # input_table = "/home/pape/Downloads/segmentedData-Tim-102219-Pos42-1error-sqrt6-2020-05-22.csv"
    input_table = "./data/pos42/tables/transcriptome/default.tsv"
    table = pd.read_csv(input_table, sep="\t")
    table["z"] = table["z"].astype("float64")
    if point_fraction is not None:
        print(table.shape)
        n_rows = int(point_fraction * len(table))
        if shuffle:
            table = table.sample(frac=1)
        table = table[:n_rows]
        print(table.shape)

    if "spot_id" not in table.columns:
        table["spot_id"] = list(range(1, len(table) + 1))
    table.to_csv(table_path, index=False, sep="\t", float_format="%.4f")

    metadata = mobie.metadata.read_dataset_metadata(ds_folder)
    metadata["sources"][name] = {
        "spots": {
            "boundingBoxMax": [225.28, 225.28, 24.0],
            "boundingBoxMin": [0.0, 0.0, 0.0],
            "tableData": {"tsv": {"relativePath": f"tables/{name}"}},
            "unit": "micrometer",
        },
    }
    mobie.metadata.write_dataset_metadata(ds_folder, metadata)


def add_spot_display(name):
    ds_folder = "./data/pos42"

    spot_view = {
        "uiSelectionGroup": "spots",
        "isExclusive": False,
        "sourceDisplays": [
            {
                "spotDisplay": {
                    "lut": "glasbey",
                    "name": name,
                    "opacity": 1.0,
                    "sources": [name],
                    "spotRadius": 0.25,
                }
            }
        ]
    }

    metadata = mobie.metadata.read_dataset_metadata(ds_folder)
    metadata["views"][name] = spot_view
    mobie.metadata.write_dataset_metadata(ds_folder, metadata)


def add_spots(small, shuffle=False):
    name = "transcriptome-small" if small else "transcriptome"
    if shuffle:
        name += "-alt"
    point_fraction = 0.1 if small else None
    add_spot_source(name, point_fraction=point_fraction, shuffle=shuffle)
    add_spot_display(name)


def add_combined_view():
    ds_folder = "./data/pos42"
    metadata = mobie.metadata.read_dataset_metadata(ds_folder)

    combined_view = metadata["views"]["default"]
    combined_view["isExclusive"] = True
    combined_view["sourceDisplays"].append(
        {
            "spotDisplay": {
                "name": "transcriptome-small",
                "sources": ["transcriptome-small"],
            }
        }
    )

    metadata["views"]["image_and_spots"] = combined_view
    mobie.metadata.write_dataset_metadata(ds_folder, metadata)


def main():
    add_spots(True, True)
    # add_spots(False)
    # add_spots(True)
    # add_combined_view()


if __name__ == "__main__":
    main()
