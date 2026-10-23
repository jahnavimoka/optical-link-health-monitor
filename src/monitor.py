
def assess_link(telemetry):
    """Classify the simulated optical link's health."""

    signal_power = telemetry["signal_power_dbm"]
    ber = telemetry["ber"]
    latency = telemetry["latency_ms"]

    faults = []

    if signal_power < -7.0:
        faults.append("LOW_SIGNAL_POWER")

    if ber > 1e-6:
        faults.append("HIGH_BIT_ERROR_RATE")

    if latency > 10.0:
        faults.append("HIGH_LATENCY")

    if signal_power < -9.0:
        status = "DOWN"
    elif faults:
        status = "DEGRADED"
    else:
        status = "HEALTHY"

    return {
        "status": status,
        "faults": faults,
    }
