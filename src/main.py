from src.event_logger import log_event
from src.simulator import generate_telemetry
from src.monitor import assess_link


def main():
    scenarios = [
        "normal",
        "low_signal",
        "high_ber",
        "high_latency",
        "link_down",
    ]

    print("OPTICAL LINK HEALTH MONITOR")
    print("=" * 40)

    for scenario in scenarios:
        telemetry = generate_telemetry(scenario)
        result = assess_link(telemetry)
        log_event(telemetry, result)

        print(f"\nScenario: {scenario}")
        print(f"Signal power: {telemetry['signal_power_dbm']} dBm")
        print(f"BER: {telemetry['ber']:.2e}")
        print(f"Latency: {telemetry['latency_ms']} ms")
        print(f"Link status: {result['status']}")
        print("Faults:", ", ".join(result["faults"]) or "None")


if __name__ == "__main__":
    main()
