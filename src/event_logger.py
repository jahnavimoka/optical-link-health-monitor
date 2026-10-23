
import csv
from pathlib import Path


LOG_FILE = Path("logs") / "link_events.csv"


def log_event(telemetry, result):
    """Append one monitoring result to the CSV event log."""

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    file_exists = LOG_FILE.exists()

    with LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "timestamp",
                "signal_power_dbm",
                "ber",
                "latency_ms",
                "status",
                "faults",
            ],
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "timestamp": telemetry["timestamp"],
            "signal_power_dbm": telemetry["signal_power_dbm"],
            "ber": telemetry["ber"],
            "latency_ms": telemetry["latency_ms"],
            "status": result["status"],
            "faults": ";".join(result["faults"]) or "None",
        })
