import unittest

from utils.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):

    def test_initialization(self):

        handler = FileHandler()

        self.assertIsNotNone(handler)


if __name__ == "__main__":
    unittest.main()