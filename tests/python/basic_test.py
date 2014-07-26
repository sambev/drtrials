import os
import unittest


class BasicTest(unittest.TestCase):

    def setUp(self):
        """ setup test app and get a handle to the database """
        pass

    def tearDown(self):
        """Clean up the database"""
        # self.db.problems.remove()
        pass

if __name__ == '__main__':
    unittest.main()
