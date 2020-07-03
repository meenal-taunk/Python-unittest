from unittest.mock import patch


class Foo:
    x = 20

    def bar(self):
        y = 10
        return y


with patch('__main__.Foo') as mock_foo:
    print(dir(mock_foo))

#Output:
'''['assert_any_call', 'assert_called', 'assert_called_once', 'assert_called_once_with', 'assert_called_with', 
'assert_has_calls', 'assert_not_called', 'attach_mock', 'call_args', 'call_args_list', 'call_count', 'called', 
'configure_mock', 'method_calls', 'mock_add_spec', 'mock_calls', 'reset_mock', 'return_value', 'side_effect']'''
