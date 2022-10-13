import mobie
import pandas as pd


def add_grid_view():
    ds_folder = "./data/pos42"
    sources = [["membrane-marker1", "transcriptome-small"], ["membrane-marker2", "transcriptome-small-alt"]]
    view_name = "grid-view"

    table_source = "positions"
    table = pd.DataFrame.from_dict({
        "region_id": [0, 1],
        "position_name": ["pos1", "pos2"],
    })
    mobie.metadata.add_regions_to_dataset(ds_folder, table_source, table)

    grid_view = mobie.metadata.get_grid_view(
        ds_folder, view_name, sources,
        menu_name="bookmarks", table_source=table_source,
    )
    mobie.metadata.add_view_to_dataset(ds_folder, view_name, grid_view)


add_grid_view()
