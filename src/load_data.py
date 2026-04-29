from pathlib import Path

import pandas as pd


DEFAULT_CSV_PATH = Path(
    "data/raw/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

USE_COLUMNS = [
    "Label",
    "Destination Port",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Packet Length Mean",
]


def load_data(csv_path=DEFAULT_CSV_PATH):
    # CSV를 읽고 컬럼명 앞뒤 공백을 제거한다.
    df = pd.read_csv(csv_path, low_memory=False)
    df.columns = df.columns.str.strip()

    # 분석에 필요한 핵심 컬럼 10개만 선택한다.
    missing_columns = [column for column in USE_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    return df[USE_COLUMNS]


if __name__ == "__main__":
    data = load_data()
    print(data.head())
    print(data.shape)
