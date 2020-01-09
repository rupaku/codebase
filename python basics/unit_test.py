''' unittest

'''
import unittest
import utility

class TestMain(unittest.TestCase):
    def setUp(self): #calls before each test case
        print('about to start a function')
    # def test_do_stuff(self):
    #     test_param=10
    #     res=utility.do_stuff(test_param)
    #     self.assertEqual(res,15)

    # def test_do_stuff2(self):
    #     test_param='rupa'
    #     res=utility.do_stuff(test_param)
    #     self.assertEqual(res,ValueError)
    #
    # def test_do_stuff3(self):
    #     test_param='rupa'
    #     res=utility.do_stuff(test_param)
    #     self.assertTrue(isinstance(res,ValueError))

    def test_do_stuff4(self):
        test_param=None
        res=utility.do_stuff(test_param)
        self.assertEqual(res,'please enter a num')

    def test_do_stuff5(self):
        test_param=''
        res=utility.do_stuff(test_param)
        self.assertEqual(res,'please enter a num')

    def tearDown(self): #calls after each test case
        print('cleaning up')

if __name__ == "__main__":
    unittest.main()

#to run all testcases file on path
# python -m unitest

#to get all info
# python -m unitest -v