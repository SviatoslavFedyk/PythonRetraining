import functions.time_operations as task_func
import pytest

@pytest.mark.parametrize("hours, expected_minutes", [(1.5, 90), (2.25, 135),
                                                     (0.75, 45), (0, 0), (24, 1440)])
def test_to_minutes(hours, expected_minutes):
    assert task_func.to_minutes(hours) == expected_minutes

@pytest.mark.parametrize("minutes, expected_hours",
                         [(90, 1.5), (120, 2.0), (45, 0.75),
                          (0, 0), (360, 6.0), (12, 0.2), (5, 0.0833)])
def test_to_hours(minutes, expected_hours):
    assert task_func.to_hours(minutes) == expected_hours