import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        print("开始测试")

    def tearDown(self):
        print("结束测试")

    def test_init(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
