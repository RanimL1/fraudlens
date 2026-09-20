from pathlib import Path

import pandas as pd
import yaml


def load_config(path="configs/config.yaml"):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def csv_to_parquet(raw_path, out_path):
    df = pd.read_csv(raw_path)
    df = df.drop(columns=["isFlaggedFraud"])  # drapeau produit par la simulation : fuite
    df["type"] = df["type"].astype("category")
    df["step"] = df["step"].astype("int16")
    df["isFraud"] = df["isFraud"].astype("int8")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(out_path, index=False)
    return df


def main():
    cfg = load_config()
    df = csv_to_parquet(cfg["data"]["raw_path"], cfg["data"]["processed_path"])
    print(f"{len(df):,} lignes, {df['isFraud'].mean():.4%} de fraudes")


if __name__ == "__main__":
    main()