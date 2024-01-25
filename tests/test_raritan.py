import unittest

from src.driver import RaritanShellDriver


class TestCheckPointGaiaFirewallShell2GDriver(unittest.TestCase):
    def setUp(self):
        self._instance = RaritanShellDriver()

    def test_init(self):
        self.assertIsNone(self._instance._cli)
