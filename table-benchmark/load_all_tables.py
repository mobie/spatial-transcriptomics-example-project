import argparse
# import os
import time

import numpy as np
import pandas as pd
# import requests


def _load_local(n_rounds):
    table_path = "../data/pos42/tables/transcriptome/default.tsv"
    times = []
    for _ in range(n_rounds):
        t0 = time.time()
        pd.read_csv(table_path, sep="\t")
        times.append(time.time() - t0)
    print("Loading a many table locally took:")
    print("Min:", np.min(times), "s")
    print("Max:", np.max(times), "s")
    print("Mean:", np.mean(times), "+-", np.std(times), "s")


def _load_remote(n_rounds):
    raise NotImplementedError


def load_many_table(local, n_rounds):
    if local:
        _load_local(n_rounds)
    else:
        _load_remote(n_rounds)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--local", default=1, type=int, help="Load the table locally or from github")
    parser.add_argument("-n", "--n_rounds", type=int, default=5, help="Number of rounds for statistics")
    args = parser.parse_args()
    load_many_table(bool(args.local), args.n_rounds)


if __name__ == "__main__":
    main()
