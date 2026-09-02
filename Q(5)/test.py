from Vec import Vec


print("Q(5) SUCCESS CASES")

vector = Vec((1, 2.345678, -3))  # Expected: (1, 2.345678, -3)
assert vector.ele == (1, 2.345678, -3)
print("__init__:", vector, "-> SUCCESS")

empty = Vec()  # Expected: ()
assert empty.ele == ()
print("empty Vec:", empty, "-> SUCCESS")

assert repr(vector) == "(1, 2.345678, -3)"  # Expected: (1, 2.345678, -3)
assert len(vector) == 3  # Expected: 3
print("__repr__:", repr(vector), "-> SUCCESS")
print("__len__:", len(vector), "-> SUCCESS")

other = Vec((4, 5, 6))
assert (vector + other).ele == (5, 7.34568, 3)  # Expected: (5, 7.34568, 3)
assert (vector + 2).ele == (3, 4.34568, -1)  # Expected: (3, 4.34568, -1)
print("Vec + Vec:", vector + other, "-> SUCCESS")
print("Vec + number:", vector + 2, "-> SUCCESS")

assert (2 + vector).ele == (3, 4.34568, -1)  # Expected: (3, 4.34568, -1)
print("number + Vec:", 2 + vector, "-> SUCCESS")

assert (2 * vector).ele == (2, 4.69136, -6)  # Expected: (2, 4.69136, -6)
print("number * Vec:", 2 * vector, "-> SUCCESS")

changed = Vec((1, 2, 3))
changed *= 2  # Expected: (2, 4, 6)
assert changed.ele == (2, 4, 6)
print("Vec *= number:", changed, "-> SUCCESS")

assert (vector - other).ele == (-3, -2.65432, -9)  # Expected: (-3, -2.65432, -9)
assert (vector - 2).ele == (-1, 0.34568, -5)  # Expected: (-1, 0.34568, -5)
print("Vec - Vec:", vector - other, "-> SUCCESS")
print("Vec - number:", vector - 2, "-> SUCCESS")

assert (2 - vector).ele == (1, -0.34568, 5)  # Expected: (1, -0.34568, 5)
print("number - Vec:", 2 - vector, "-> SUCCESS")

changed = Vec((5, 6, 7))
changed -= other  # Expected: (1, 1, 1)
assert changed.ele == (1, 1, 1)
print("Vec -= Vec:", changed, "-> SUCCESS")
changed += other  # Expected: (5, 6, 7)
assert changed.ele == (5, 6, 7)
print("Vec += Vec:", changed, "-> SUCCESS")

assert (-vector).ele == (-1, -2.34568, 3)  # Expected: (-1, -2.34568, 3)
print("-Vec:", -vector, "-> SUCCESS")

assert Vec.zeros(3).ele == (0, 0, 0)  # Expected: (0, 0, 0)
assert Vec.ones(3).ele == (1, 1, 1)  # Expected: (1, 1, 1)
random_vector = Vec.uniform(3)
assert len(random_vector) == 3
assert all(0 <= value < 1 for value in random_vector.ele)
print("Vec.zeros(3):", Vec.zeros(3), "-> SUCCESS")
print("Vec.ones(3):", Vec.ones(3), "-> SUCCESS")
print("Vec.uniform(3):", random_vector, "-> SUCCESS")

assert Vec((3, 4)).norm() == 5.0  # Expected: 5.0
print("norm:", Vec((3, 4)).norm(), "-> SUCCESS")


print("\nQ(5) EXPECTED FAILURE CASES")

try:
    Vec((1, "text"))
except TypeError as error:
    print("invalid value:", error, "-> EXPECTED FAILURE")
else:
    raise AssertionError("invalid vector value was accepted")

try:
    vector + "text"
except TypeError as error:
    print("Vec + text:", error, "-> EXPECTED FAILURE")
else:
    raise AssertionError("invalid addition was accepted")

try:
    "text" * vector
except TypeError as error:
    print("text * Vec:", error, "-> EXPECTED FAILURE")
else:
    raise AssertionError("invalid multiplication was accepted")

try:
    vector - "text"
except TypeError as error:
    print("Vec - text:", error, "-> EXPECTED FAILURE")
else:
    raise AssertionError("invalid subtraction was accepted")

try:
    vector + Vec((1, 2))
except TypeError as error:
    print("different vector lengths:", error, "-> EXPECTED FAILURE")
else:
    raise AssertionError("different vector lengths were accepted")

print("\nQ(5) all tests passed")
