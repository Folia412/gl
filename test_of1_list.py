import unittest


class TestListNumber(unittest.TestCase):
    def oftest1(self):
        self.assertIs(["j"], ["j"])
        self.assertIs(["-2"], ["-3"])

    def oftest2(self):
        self.assertIsNot(["k", "z", "l"], ["k", "l", "z"])

if __name__ == '__main__':
    unittest.main()
