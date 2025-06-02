# 🚫 Before:
def test_sum():
    assert sum([1, 2, 3]) == 6
    assert sum([1, 1, 1]) == 3
    assert sum([0, 0, 0]) == 0


# ✅ After:
import pytest


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([1, 2, 3], 6),
        ([1, 1, 1], 3),
        ([0, 0, 0], 0),
    ],
)
def test_sum(numbers, expected):
    assert sum(numbers) == expected


# 🧠 ➤ @pytest.mark.parametrize makes tests cleaner, easier to scale, and improves debugging by showing each case separately.
