import unittest

from WasRun import WasRun


class TestCaseTest(unittest.TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasSetUp)

TestCaseTest("testRunning").run()



if __name__ == '__main__':
    unittest.main()
