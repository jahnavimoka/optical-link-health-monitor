
import random
import time


def generate_telemetry(scenario="normal"):
    """Generate simulated optical link measurements."""

    if scenario == "normal":
        signal_power = random.uniform(-5.0, -2.0)
        ber = 10 ** random.uniform(-9, -7)
        latency_ms = random.uniform(1.0, 5.0)

    elif scenario == "low_signal":
        signal_power = random.uniform(-10.0, -7.5)
        ber = 10 ** random.uniform(-8, -6)
        latency_ms = random.uniform(1.0, 5.0)

    elif scenario == "high_ber":
        signal_power = random.uniform(-5.0, -2.0)
        ber = 10 ** random.uniform(-5, -4)
        latency_ms = random.uniform(1.0, 5.0)

    elif scenario == "high_latency":
        signal_power = random.uniform(-5.0, -2.0)
        ber = 10 ** random.uniform(-9, -7)
        latency_ms = random.uniform(12.0, 25.0)

    elif scenario == "link_down":
        signal_power = random.uniform(-12.0, -10.0)
        ber = 10 ** random.uniform(-4, -3)
        latency_ms = random.uniform(20.0, 50.0)

    else:
        raise ValueError(f"Unknown scenario: {scenario}")

    return {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "signal_power_dbm": round(signal_power, 2),
        "ber": ber,
        "latency_ms": round(latency_ms, 2),
    }


if __name__ == "__main__":
    for scenario in ["normal", "low_signal", "high_ber",
                     "high_latency", "link_down"]:
        telemetry = generate_telemetry(scenario)
        print(f"\nScenario: {scenario}")
        print(telemetry)
