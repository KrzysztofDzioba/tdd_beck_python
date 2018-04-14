import unittest

from WasRun import WasRun


class Tests(unittest.TestCase):

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FoO')

    test = WasRun("testMethod")
    print (test.wasRun)
    test.run()
    print (test.wasRun)



if __name__ == '__main__':
    unittest.main()
