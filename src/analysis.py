from preprocess import preprocess_data


def run_analysis():
    df = preprocess_data()
    binary_counts = df["Binary Label"].value_counts().sort_index()
    attack_distribution = df["Label"].value_counts()
    port_top10 = df["Destination Port"].value_counts().head(10)

    print("Binary Label Counts")
    print(binary_counts)

    print("\nAttack Type Distribution")
    print(attack_distribution)

    print("\nTop 10 Destination Ports")
    print(port_top10)

    return binary_counts, attack_distribution, port_top10


if __name__ == "__main__":
    run_analysis()
