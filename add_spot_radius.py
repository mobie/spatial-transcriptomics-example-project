import mobie

ds_folder = "./data/pos42-spatial-transcriptomics"
metadata = mobie.metadata.read_dataset_metadata(ds_folder)

new_views = {}
spot_radius = 0.25
for name, view in metadata["views"].items():

    new_displays = []
    for display in view["sourceDisplays"]:
        display_type, display_data = next(iter(display.items()))
        if display_type == "spotDisplay":
            display_data["spotRadius"] = spot_radius
            display = {display_type: display_data}
        new_displays.append(display)
    view["sourceDisplays"] = new_displays

    new_views[name] = view

metadata["views"] = new_views
mobie.metadata.write_dataset_metadata(ds_folder, metadata)
