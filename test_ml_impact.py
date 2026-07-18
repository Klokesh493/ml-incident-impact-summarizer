import unittest

from ml_impact import summarize


class MLImpactTest(unittest.TestCase):
    def test_rolls_up_affected_users(self):
        rows = [{"model": "m", "endpoint": "/a", "affected_users": "8000"}, {"model": "m", "endpoint": "/b", "affected_users": "3500"}]
        self.assertEqual(summarize(rows)["severity"], "sev1")


if __name__ == "__main__":
    unittest.main()
