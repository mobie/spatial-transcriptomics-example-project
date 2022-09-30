import zarr

path = "./data/pos42-spatial-transcriptomics/images/ome-zarr/MMStack_Pos42.ome.zarr"
with zarr.open(path, "r") as f:
    attrs = f.attrs["multiscales"][0]
    scale = attrs["datasets"][0]["coordinateTransformations"][0]["scale"]
    shape = f["0"].shape

unit = attrs["axes"][1]["unit"]
print(unit)
print()
print(scale)
print(shape)
print()
extent = [sc * sh for sc, sh in zip(scale[1:], shape[1:])]
print(extent)
