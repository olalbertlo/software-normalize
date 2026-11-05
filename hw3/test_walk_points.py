import pytest

from hw3.walk_points import walk_points


@pytest.mark.parametrize(
    ("laps", "expected"),
    [(0, 0), (1, 1), (4, 3)],
    ids=["T1", "T2", "T3"],
)
def test_walk_points(laps, expected):
    result = walk_points(laps)
    print(f"laps={laps}, expected={expected}, result={result}")
    assert result == expected
