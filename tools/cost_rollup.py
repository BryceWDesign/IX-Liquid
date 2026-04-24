from __future__ import annotations

import csv
from pathlib import Path


def rollup_bom(csv_path: str) -> tuple[float, float]:
    low_total = 0.0
    high_total = 0.0
    with Path(csv_path).open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            low_total += float(row["extended_low_usd"])
            high_total += float(row["extended_high_usd"])
    return low_total, high_total


if __name__ == "__main__":
    low, high = rollup_bom("bom/ix_liquid_bom.csv")
    print(f"Low estimate: ${low:,.0f}")
    print(f"High estimate: ${high:,.0f}")
