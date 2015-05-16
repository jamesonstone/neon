import unittest
from hello_world import HelloWorld


class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello_world(self):
        self.assertEquals(HelloWorld().hello('jameson'), 'hello there, jameson')

    def test_hello_world_number(self):
        self.assertEqual(HelloWorld().hello(1), 'hello there, 1')

    def test_hello_world_wrong_input(self):
        self.assertNotEqual(HelloWorld().hello('jameson'), 'hello there, dog')




if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorld)
    unittest.TextTestRunner(verbosity=2).run(suite)