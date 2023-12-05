import functions.math_operations as task_func
from helper.custom_exceptions import *
import pytest

@pytest.mark.parametrize("num1, num2, expected_result", [(2, 3, False), (12, 3, True),
                                                         (25, 5, True), (7, 2, False), (100, 10, True)])
def test_is_whole_div(num1, num2, expected_result):
    assert task_func.is_whole_div(num1, num2) == expected_result

@pytest.mark.parametrize("num1, num2, expected_result", [(-2, 3, NonPositiveIntegerException), (12, -3, NonPositiveIntegerException)])
def negative_test_is_whole_div(num1, num2, expected_result):
    with pytest.raises(expected_result) as e_info:
        task_func.is_whole_div(num1, num2)

@pytest.mark.parametrize("arr, expected_result", [ ([1,2,4,4,6,6,3,3,34,65,7], [11, 8, 5, [3, 4, 6], 2]),
                                                   ([-6,34,34,6,0], [5, 4, 3, [34], 2]),
                                                   ([-6,34.15,34.15,6,0], [0, 0, 0, [], 0]),
                                                    (3,[0, 0, 0, [], 0])])
def test_stat(arr, expected_result):
    assert task_func.stat(arr) == expected_result