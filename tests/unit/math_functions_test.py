import functions.math_operations as task_func
import pytest

@pytest.mark.parametrize("num1, num2, expected_result", [(2, 3, False), (12, 3, True),
                                                         (25, 5, True), (7, 2, False), (100, 10, True)])
def test_is_whole_div(num1, num2, expected_result):
    assert task_func.is_whole_div(num1, num2) == expected_result