from test_vector import Vec

# 1. mean()
x = Vec((1, 2, 3, 4, 5))

assert x.mean() == 3.0
print("mean():", x.mean())


# 2. demean()
de_meaned = x.demean()
assert de_meaned.ele == (-2.0, -1.0, 0.0, 1.0, 2.0)
print("demean():", de_meaned)


# Property: mean of a de-meaned vector should be zero
assert abs(de_meaned.mean()) < 1e-10
print("mean(demean(x)) == 0")


# Property: de-meaned vector should have the same length
assert len(de_meaned) == len(x)
print("demean() preserves length ->")


# 3. std()
# For (1, 2, 3, 4, 5):
# mean = 3
# squared deviations = 4, 1, 0, 1, 4
# average = 2
# std = sqrt(2)
expected_std = 2 ** 0.5
assert abs(x.std() - expected_std) < 1e-10
print("std():", x.std())


# Property: standard deviation cannot be negative
assert x.std() >= 0
print("std() is non-negative ->")


# Constant vector should have standard deviation 0
constant = Vec((5, 5, 5, 5))

assert constant.std() == 0.0
print("std() of constant vector:", constant.std())



# 4. Empty-vector failure cases
try:
    Vec().mean()
except ValueError as error:
    print("mean() on empty vector:", error,)
else:
    raise AssertionError("mean() should reject an empty vector")


try:
    Vec().std()
except ValueError as error:
    print("std() on empty vector:", error,)
else:
    raise AssertionError("std() should reject an empty vector")


print("\nAll tests passed")
