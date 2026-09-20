import pandas as pd

from fraudlens.data.loader import csv_to_parquet


def test_csv_to_parquet_drops_flag(tmp_path):
    raw = tmp_path / "raw.csv"
    pd.DataFrame(
        {
            "step": [1, 2],
            "type": ["TRANSFER", "CASH_OUT"],
            "amount": [100.0, 50.0],
            "nameOrig": ["C1", "C2"],
            "oldbalanceOrg": [100.0, 50.0],
            "newbalanceOrig": [0.0, 0.0],
            "nameDest": ["C3", "C4"],
            "oldbalanceDest": [0.0, 0.0],
            "newbalanceDest": [100.0, 50.0],
            "isFraud": [1, 0],
            "isFlaggedFraud": [0, 0],
        }
    ).to_csv(raw, index=False)

    out = tmp_path / "out.parquet"
    df = csv_to_parquet(raw, out)

    assert "isFlaggedFraud" not in df.columns
    assert out.exists()
    assert len(pd.read_parquet(out)) == 2