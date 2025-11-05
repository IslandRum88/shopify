import unittest
from main import vacuum_movements

class TestVacMovement(unittest.TestCase):

    def test_obstacle(self):
        result = vacuum_movements()
        self.assertEquals(result, 25)

    def test_return_int(self):
        result = vacuum_movements()
        self.assertIsInstance(result, int)

