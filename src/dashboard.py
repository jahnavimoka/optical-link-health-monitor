
import csv
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


LOG_FILE = Path("logs") / "link_events.csv"


def load_events():
    """Read saved monitoring records from the CSV log."""
    if not LOG_FILE.exists():
        raise FileNotFoundError(
            "No event log found. Run python -m src.main first."
        )

    with LOG_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def plot_dashboard():
    events = load_events()

    if not events:
        print("No monitoring records available.")
        return

    scenarios = [f"Reading {i}" for i in range(1, len(events) + 1)]
    signal_power = [float(e["signal_power_dbm"]) for e in events]
    ber = [float(e["ber"]) for e in events]
    latency = [float(e["latency_ms"]) for e in events]
    statuses = [e["status"] for e in events]

    counts = Counter(statuses)

    print("\nOPTICAL LINK HEALTH SUMMARY")
    print("-" * 30)
    print(f"Total readings: {len(events)}")
    for status in ("HEALTHY", "DEGRADED", "DOWN"):
        print(f"{status}: {counts.get(status, 0)}")

    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle(
        f"Optical Link Health Monitor | {len(events)} readings",
        fontsize=15,
    )

    axes[0].plot(scenarios, signal_power, marker="o")
    axes[0].axhline(-7, linestyle="--", label="Low-signal warning")
    axes[0].axhline(-9, linestyle=":", label="DOWN threshold")
    axes[0].set_ylabel("Signal power (dBm)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].semilogy(scenarios, ber, marker="o")
    axes[1].axhline(1e-6, linestyle="--", label="BER threshold")
    axes[1].set_ylabel("Bit error rate (BER)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(scenarios, latency, marker="o")
    axes[2].axhline(10, linestyle="--", label="Latency threshold")
    axes[2].set_ylabel("Latency (ms)")
    axes[2].set_xlabel("Monitoring record")
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_dashboard()
