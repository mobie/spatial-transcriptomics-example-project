import os
from shutil import copytree

import mobie
import numpy as np
from elf.io import open_file


def copy_if_necessary(data_path, dataset):
    fname = os.path.basename(data_path)
    out_path = os.path.join("./data", dataset, "images", "ome-zarr", fname)
    if os.path.exists(out_path):
        return out_path
    copytree(data_path, out_path)
    return out_path


def compute_contrast_limits(ds, channel_id):
    data = ds[channel_id][:]
    cmin, cmax = np.percentile(data, 5), np.percentile(data, 95)
    return [cmin, cmax]


# NOTE: this needs experimental functionality from the "channel" branch in
# mobie-utils-python
def create_example_project(dataset_name):
    root = "./data"
    data_path = "/home/pape/Downloads/MMStack_Pos42.ome.zarr"

    channel_names = ["membrane-marker1", "membrane-marker2", "membrane-marker3", "nuclei"]
    with open_file(data_path, "r") as f:
        ds = f["0"]
        n_channels = ds.shape[0]

        assert n_channels == len(channel_names)
        for channel_id in range(n_channels):
            image_name = channel_names[channel_id]
            contrast_limits = compute_contrast_limits(ds, channel_id)
            view = mobie.utils.require_dataset_and_view(root, dataset_name=dataset_name, file_format="ome.zarr",
                                                        source_type="image", source_name=image_name,
                                                        menu_name="image-data",
                                                        is_default_dataset=False,
                                                        view=None,
                                                        contrast_limits=contrast_limits)
            image_path = copy_if_necessary(data_path, dataset_name)
            mobie.metadata.add_source_to_dataset(os.path.join(root, dataset_name), "image", image_name, image_path,
                                                 view=view, description=None, channel=channel_id)


if __name__ == "__main__":
    create_example_project("pos42-spatial-transcriptomics")
