from hypothesis import example, given, settings
from hypothesis.strategies import integers
import pytest


def broken_sum(a: int, b: int) -> int:
    wrong_case = 3
    if a == wrong_case or b == wrong_case:
        return 0
    return a + b


@settings(max_examples=50000, report_multiple_bugs=True, print_blob=True)
@given(integers(), integers())
@example(1, 1)
def test_broken_sum(a, b):
    assert broken_sum(a, b) == a + b
