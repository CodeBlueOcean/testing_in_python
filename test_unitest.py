import unittest
import script_unitest

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
    def test_do_stuff(self):
        test_param = 10 
        result = script_unitest.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = 'shkshks'
        result = script_unitest.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = script_unitest.do_stuff(test_param)
        self.assertEqual(result,'please enter number_')
    
    def test_do_stuff4(self):
        test_param = None
        result = script_unitest.do_stuff(test_param)
        self.assertEqual(result,'please enter number_')

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()



