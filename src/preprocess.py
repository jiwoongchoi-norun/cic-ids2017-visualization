import numpy as np

from load_data import load_data


def preprocess_data(csv_path=None):
    df = load_data(csv_path).copy() if csv_path else load_data().copy()

    # Label 공백을 제거한다.
    df["Label"] = df["Label"].str.strip()

    # BENIGN은 정상, 그 외는 공격으로 이진 라벨을 만든다.
    df["Binary Label"] = np.where(df["Label"] == "BENIGN", 0, 1)

    # inf 값을 NaN으로 바꾼 뒤 제거한다.
    speed_columns = ["Flow Bytes/s", "Flow Packets/s"]
    df[speed_columns] = df[speed_columns].replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=["Flow Bytes/s", "Flow Packets/s"])

    return df


if __name__ == "__main__":
    data = preprocess_data()
    print(data.head())
    print(data.shape)
