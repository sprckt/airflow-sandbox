#! /usr/bin/env python3

import pandas as pd
from pathlib import Path


def main():

    base_path = Path.cwd().parent

    print(f"Path: r{base_path}")
    source_file_path = base_path / "stages" / "landing" / "housing-density-borough.csv"
    destination_file_path = base_path.joinpath("stages", "staging", "cleaned.parquet")
    print(f"Reading from: {source_file_path} and writing to: {destination_file_path}")

    raw = pd.read_csv(source_file_path)
    print(f"Data count: {raw.count()}")

    raw.to_parquet(destination_file_path)


if __name__ == "__main__":
    main()
