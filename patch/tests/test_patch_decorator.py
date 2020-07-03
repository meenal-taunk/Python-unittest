from unittest import TestCase, mock
from src import fs


class TestExample(TestCase):
    @mock.patch('src.fs.check_output', return_value=b'foo\nbar\n')
    def test_print_contents_of_cwd(self, mock_check_output):
        actual_result = fs.print_contents_of_cwd()
        expected_result = b'bar'
        self.assertIn(expected_result,actual_result)

