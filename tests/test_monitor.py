
import unittest

from src.monitor import assess_link
from src.simulator import generate_telemetry


class TestOpticalLinkMonitor(unittest.TestCase):

    def test_normal_link_is_healthy(self):
        telemetry = generate_telemetry("normal")
        result = assess_link(telemetry)

        self.assertEqual(result["status"], "HEALTHY")
        self.assertEqual(result["faults"], [])

    def test_high_ber_is_detected(self):
        telemetry = generate_telemetry("high_ber")
        result = assess_link(telemetry)

        self.assertIn("HIGH_BIT_ERROR_RATE", result["faults"])
        self.assertEqual(result["status"], "DEGRADED")

    def test_high_latency_is_detected(self):
        telemetry = generate_telemetry("high_latency")
        result = assess_link(telemetry)

        self.assertIn("HIGH_LATENCY", result["faults"])
        self.assertEqual(result["status"], "DEGRADED")

    def test_severe_signal_loss_is_down(self):
        telemetry = generate_telemetry("link_down")
        result = assess_link(telemetry)

        self.assertEqual(result["status"], "DOWN")
        self.assertIn("LOW_SIGNAL_POWER", result["faults"])

    def test_signal_at_down_threshold_is_not_down(self):
        telemetry = {
            "signal_power_dbm": -9.0,
            "ber": 1e-8,
            "latency_ms": 2.0,
        }

        result = assess_link(telemetry)

        self.assertEqual(result["status"], "DEGRADED")
        self.assertIn("LOW_SIGNAL_POWER", result["faults"])
        
    def test_signal_at_warning_threshold_is_not_low_signal(self):
        telemetry = {
            "signal_power_dbm": -7.0,
            "ber": 1e-8,
            "latency_ms": 5.0,
        }

        result = assess_link(telemetry)

        self.assertNotIn("LOW_SIGNAL_POWER", result["faults"])
        self.assertEqual(result["status"], "HEALTHY")

    def test_ber_at_threshold_is_not_high_ber(self):
        telemetry = {
            "signal_power_dbm": -5.0,
            "ber": 1e-6,
            "latency_ms": 5.0,
        }

        result = assess_link(telemetry)

        self.assertNotIn("HIGH_BIT_ERROR_RATE", result["faults"])
        self.assertEqual(result["status"], "HEALTHY")
        
    def test_multiple_faults_are_detected_together(self):
        telemetry = {
            "signal_power_dbm": -10.0,
            "ber": 1e-4,
            "latency_ms": 20.0,
        }

        result = assess_link(telemetry)

        self.assertEqual(result["status"], "DOWN")
        self.assertIn("LOW_SIGNAL_POWER", result["faults"])
        self.assertIn("HIGH_BIT_ERROR_RATE", result["faults"])
        self.assertIn("HIGH_LATENCY", result["faults"])
        
    def test_unknown_scenario_raises_error(self):
        with self.assertRaises(ValueError):
            generate_telemetry("unknown_scenario")






if __name__ == "__main__":
    unittest.main()
