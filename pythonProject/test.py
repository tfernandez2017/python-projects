import unittest
import script1

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a function')

    def test_do_stuff(self):
        test_param = 10
        result = script1.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'dfgdfggh'
        result = script1.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = (script1.do_stuff(test_param))
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = script1.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff5(self):
        test_param = 0
        result = script1.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

    def tearDown(self):
        print('cleaning up')

