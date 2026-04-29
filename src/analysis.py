from preprocess import preprocess_data


def run_analysis():
    df = preprocess_data()
    binary_counts = df["Binary Label"].value_counts().sort_index()
    binary_percentages = (binary_counts / len(df) * 100).round(2)
    attack_distribution = df["Label"].value_counts()
    attack_percentages = (attack_distribution / len(df) * 100).round(2)
    port_top10 = df["Destination Port"].value_counts().head(10)

    print("Binary Label Counts")
    print(binary_counts)

    print("\nBinary Label Percentages")
    print(binary_percentages)

    print("\nAttack Type Distribution")
    print(attack_distribution)

    print("\nAttack Type Percentages")
    print(attack_percentages)

    print("\nTop 10 Destination Ports")
    print(port_top10)

    return (
        binary_counts,
        binary_percentages,
        attack_distribution,
        attack_percentages,
        port_top10,
    )


if __name__ == "__main__":
    run_analysis()
