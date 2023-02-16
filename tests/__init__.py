import unittest


def suite():
    test_suite = unittest.TestSuite()
    # add all the tests here
    test_suite.addTest(unittest.makeSuite(test_cake_aligner.TestCakeAligner))
    return test_suite


if __name__ == "__main__":
    unittest.main()
