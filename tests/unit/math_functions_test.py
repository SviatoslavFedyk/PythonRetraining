import functions.math_operations as task_func
import pytest

@pytest.mark.parametrize("num1, num2, expected_result", [(2, 3, False), (12, 3, True),
                                                         (25, 5, True), (7, 2, False), (100, 10, True)])
def test_is_whole_div(num1, num2, expected_result):
    assert task_func.is_whole_div(num1, num2) == expected_result

@pytest.mark.parametrize("arr, expected_result", [ ([1,2,4,4,6,6,3,3,34,65,7], [11, 8, 5, [3, 4, 6], 2]),
                                                   ([-6,34,34,6,0], [5, 4, 3, [34], 2]),
                                                   ([-6,34.15,34.15,6,0], [0, 0, 0, [], 0]),
                                                    (3,[0, 0, 0, [], 0])])
def test_stat(arr, expected_result):
    assert task_func.stat(arr) == expected_result