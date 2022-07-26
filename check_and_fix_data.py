import os
import z5py


def check_data(path, group=None):
    with z5py.File(path, "r") as f:
        g = f if group is None else f[group]
        for name, ds in g.items():
            try:
                dtype = ds.dtype
                print(name, dtype)
                data = ds[:]
                print(data.min(), data.max())
            except AttributeError:
                pass


def check_all_data(ds_folder):
    data_path = os.path.join(ds_folder, "images/ome-zarr/MMStack_Pos42.ome.zarr")
    check_data(data_path)
    print()
    check_data(data_path, "labels/cells")
    print()
    check_data(data_path, "labels/nuclei")


def fix_data(path):
    with z5py.File(path, "a") as f:
        for ds_name in range(1, 5):
            ds_name = str(ds_name)
            data = f[ds_name][:].astype("uint16")
            chunks = f[ds_name].chunks
            del f[ds_name]
            f.create_dataset(ds_name, data=data, chunks=chunks, compression="gzip")


fix_data("./data/pos42/images/ome-zarr/MMStack_Pos42.ome.zarr")
fix_data("./data/pos42-spatial-transcriptomics/images/ome-zarr/MMStack_Pos42.ome.zarr")
# check_all_data("./data/pos42")
# check_all_data("./data/pos42-spatial-transcriptomics")
