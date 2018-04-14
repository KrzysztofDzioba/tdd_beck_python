import unittest

from WasRun import WasRun


class TestCaseTest(unittest.TestCase):

    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

TestCaseTest("testRunning").run()



if __name__ == '__main__':
    unittest.main()
