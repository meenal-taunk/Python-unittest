from unittest import TestCase, mock
from src import fs


class TestExample(TestCase):

    def setUp(self):
        self.patcher = mock.patch('src.fs.check_output', return_value=b'foo\nbar\n')
        self.patcher.start()

    def test_print_contents_of_cwd(self):
        actual_result = fs.print_contents_of_cwd()
        expected_result = b'bar'
        self.assertIn(expected_result,actual_result)

    def tearDown(self):
        self.patcher.stop()

