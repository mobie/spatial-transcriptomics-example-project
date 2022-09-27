import pandas as pd


def scale_table(table_path):
    scale = {"z": 4.0, "y": 0.11, "x": 0.11}
    tab = pd.read_csv(table_path, sep="\t")
    for name, sc in scale.items():
        tab[name] = tab[name] * sc
    tab.to_csv(table_path, sep="\t", float_format="%.4f", index=False)


def main():
    scale_table("./data/pos42-spatial-transcriptomics/tables/transcriptome/default.tsv")
    scale_table("./data/pos42-spatial-transcriptomics/tables/transcriptome-small/default.tsv")


if __name__ == "__main__":
    main()
