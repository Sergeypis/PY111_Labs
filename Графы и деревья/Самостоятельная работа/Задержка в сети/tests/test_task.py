import unittest

from task import network_delay_time


class TestNetworkDelayTime(unittest.TestCase):
    def test_networkDelayTime(self):
        self.assertEqual(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2)
        self.assertEqual(network_delay_time([[1,2,1],[2,3,2],[1,3,2]], 3, 1), 2)
        self.assertEqual(network_delay_time([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 3, 2), 6)
