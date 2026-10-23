
# Optical Link Health Monitor and Fault Simulator

## Overview
A Python-based simulation project that generates optical-link telemetry, monitors link health, detects threshold violations, and records fault events.

This project uses simulated measurements; it does not connect to physical optical-fibre equipment.

## Features
- Simulated optical signal power, bit-error rate (BER), and latency
- Normal, low-signal, high-BER, high-latency, and link-down scenarios
- Rule-based health classification: HEALTHY, DEGRADED, and DOWN
- CSV event logging for persistent monitoring history
- Matplotlib dashboard for telemetry visualization
- Automated unit tests using Python's unittest framework

## Project Structure
- `src/simulator.py` - generates telemetry for selected scenarios
- `src/monitor.py` - classifies link health and detects faults
- `src/event_logger.py` - appends monitoring results to a CSV file
- `src/main.py` - runs the monitoring scenarios
- `src/dashboard.py` - plots logged telemetry
- `tests/test_monitor.py` - tests monitoring behaviour
- `logs/link_events.csv` - stores monitoring records

## Requirements
- Python 3.13+
- Matplotlib

## Setup
Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the plotting dependency:

```bash
python -m pip install matplotlib
```

## Run the monitor

From the project root:

```bash
python -m src.main
```

## Run the dashboard

```bash
python -m src.dashboard
```

## Run automated tests

```bash
python -m unittest discover -s tests -v
```

## Health Classification
The current simulation rules use configurable thresholds for signal power, BER, and latency. A severe signal-power threshold triggers DOWN; other threshold violations trigger DEGRADED.

These are demonstration rules, not universal optical-network specifications.

## Limitations and Future Improvements
- Uses simulated rather than physical optical-link measurements
- Thresholds require validation against an appropriate reference specification for real deployment
- Planned improvements include richer event summaries, more boundary tests, and concurrent telemetry processing
