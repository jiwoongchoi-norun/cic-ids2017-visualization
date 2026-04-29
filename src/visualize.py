import os

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from analysis import run_analysis


def plot_results():
    binary_counts, attack_distribution, port_top10 = run_analysis()
    output_dir = "reports/figures"
    os.makedirs(output_dir, exist_ok=True)

    binary_counts.plot(kind="bar", title="Binary Label Distribution")
    plt.xlabel("Binary Label")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "binary_label_distribution.png"))
    plt.show()

    attack_distribution.plot(kind="bar", title="Attack Type Distribution")
    plt.xlabel("Label")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "attack_type_distribution.png"))
    plt.show()

    port_top10.plot(kind="bar", title="Top 10 Destination Ports")
    plt.xlabel("Destination Port")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "port_top10.png"))
    plt.show()


if __name__ == "__main__":
    plot_results()
