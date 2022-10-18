import argparse
import os
import time

import numpy as np
import pandas as pd
import requests


def _load_local(n_rounds):
    table_path = "../data/pos42/tables/transcriptome/default.parquet"
    times = []
    for _ in range(n_rounds):
        t0 = time.time()
        pd.read_parquet(table_path)
        times.append(time.time() - t0)
    print("Loading a single table locally took:")
    print("Min:", np.min(times), "s")
    print("Max:", np.max(times), "s")
    print("Mean:", np.mean(times), "+-", np.std(times), "s")


def _load_remote(n_rounds):
    table_address = "https://github.com/mobie/spatial-transcriptomics-example-project/blob/parquet/data/pos42/tables/transcriptome/default.parquet?raw=true"
    tmp_path = "./table_tmp.parquet"
    times = []
    for _ in range(n_rounds):
        t0 = time.time()
        # using streams would be more elegant...
        with requests.get(table_address) as r:
            with open(tmp_path, "wb") as f:
                f.write(r.content)
        pd.read_parquet(tmp_path)
        os.remove(tmp_path)
        times.append(time.time() - t0)
    print("Loading a single table locally took:")
    print("Min:", np.min(times), "s")
    print("Max:", np.max(times), "s")
    print("Mean:", np.mean(times), "+-", np.std(times), "s")


def load_single_table(local, n_rounds):
    if local:
        _load_local(n_rounds)
    else:
        _load_remote(n_rounds)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--local", default=1, type=int, help="Load the table locally or from github")
    parser.add_argument("-n", "--n_rounds", type=int, default=10, help="Number of rounds for statistics")
    args = parser.parse_args()
    load_single_table(bool(args.local), args.n_rounds)


if __name__ == "__main__":
    main()
