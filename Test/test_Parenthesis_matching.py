import main.Parenthesis_matching

import pytest


@pytest.mark.parametrize("test_input,expected", [('([[])]}', False), ("(){}[]", True), ("({[]})", True)])
def test_eval(test_input, expected):
    assert main.Parenthesis_matching.parenthesis_check(test_input) == expected
