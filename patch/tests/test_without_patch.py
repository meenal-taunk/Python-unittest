from unittest import TestCase, mock
from src import fs


class TestExample(TestCase):

    def test_print_contents_of_cwd(self):
        actual_result = fs.print_contents_of_cwd()
        expected_result = b'src'
        self.assertIn(expected_result, actual_result)

