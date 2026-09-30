from vec_statistics import Vec
import math


def test_mean():
    v1 = Vec([12, 18, 24, 30])
    assert abs(v1.mean() - 21) < 0.00001

    v2 = Vec([-10, 5, 15, -20])
    assert abs(v2.mean() - (-2.5)) < 0.00001

    v3 = Vec([3.5, 7.5, 11.5])
    assert abs(v3.mean() - 7.5) < 0.00001

    v4 = Vec([42])
    assert v4.mean() == 42

    v5 = Vec([8, -8, 4, -4])
    assert v5.mean() == 0

    v6 = Vec([9, 9, 9, 9])
    assert v6.mean() == 9

    v7 = Vec([0, 0, 0, 0])
    assert v7.mean() == 0


def test_demean():
    v1 = Vec([5, 10, 15, 20])
    result = v1.demean()

    assert result.ele == (-7.5, -2.5, 2.5, 7.5)
    assert len(result) == len(v1)
    assert abs(result.mean()) < 0.00001

    # Property: mean of a de-meaned vector should be zero
    assert abs(result.mean()) < 1e-10
   
    # Property: de-meaned vector should have the same length
    assert len(result) == len(v1)
  

    v2 = Vec([4, 4, 4, 4])
    result = v2.demean()

    assert result.ele == (0, 0, 0, 0)
    assert result.mean() == 0

    v3 = Vec([-6, 2, 10])
    result = v3.demean()

    assert abs(sum(result.ele)) < 0.00001
    assert abs(result.mean()) < 0.00001


def test_std():
    v1 = Vec([1, 2, 3, 4, 5])
    assert abs(v1.std() - math.sqrt(2)) < 0.00001

    # Property: standard deviation cannot be negative
    assert v1.std() >= 0

    v2 = Vec([10, 10, 10, 10])
    assert v2.std() == 0

    v3 = Vec([-5, 0, 5])
    assert abs(v3.std() - math.sqrt(50 / 3)) < 0.00001

    v4 = Vec([2, 4, 6, 8])
    expected = math.sqrt(5)
    assert abs(v4.std() - expected) < 0.00001

    v5 = Vec([0, 0, 0, 0, 0])
    assert v5.std() == 0

    # Constant vector should have standard deviation 0
    constant = Vec((5, 5, 5, 5))
    assert constant.std() == 0.0


def test_single_element():
    v = Vec([25])

    assert v.mean() == 25
    assert v.demean().ele == (0,)
    assert v.std() == 0


def test_empty_vector():
    v = Vec()

    try:
        v.mean()
    except ValueError:
        pass
    else:
        assert False

    try:
        v.std()
    except ValueError:
        pass
    else:
        assert False
