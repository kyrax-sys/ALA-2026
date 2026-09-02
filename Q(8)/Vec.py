import math
import random


class Vec:
    # Make a vector from numbers.
    def __init__(self, src=None):
        if src is None:
            self.ele = ()
        else:
            ele = tuple(src)
            for x in ele:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"Scalar must be a number: {type(x)}")
            self.ele = ele

    # Add two vectors, or add one number to every element.
    def __add__(self, other):
        if isinstance(other, Vec):
            if len(self.ele) != len(other.ele):
                raise TypeError("Vectors must have the same dimensions")
            res = ()
            for x, y in zip(self.ele, other.ele):
                res = res + (round(x + y, 5),)
            return Vec(res)
        if isinstance(other, (int, float)):
            res = ()
            for x in self.ele:
                res = res + (round(other + x, 5),)
            return Vec(res)
        raise TypeError(f"Can't add Vec and {type(other)}")

    # Multiply every element by a number and return a new vector.
    def __rmul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(other)}")
        res = ()
        for x in self.ele:
            res = res + (round(other * x, 5),)
        return Vec(res)

    # Multiply every element by a number and update this vector.
    def __imul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError(f"Vector multiplication with invalid type: {type(other)}")
        res = ()
        for x in self.ele:
            res = res + (round(x * other, 5),)
        self.ele = res
        return self

    # Show the vector as a tuple.
    def __repr__(self):
        return repr(self.ele)

    # Return the number of elements.
    def __len__(self):
        return len(self.ele)

    # Subtract two vectors, or subtract one number from every element.
    def __sub__(self, other):
        if isinstance(other, Vec):
            if len(self.ele) != len(other.ele):
                raise TypeError("Vectors must have the same dimensions")
            res = ()
            for x, y in zip(self.ele, other.ele):
                res = res + (round(x - y, 5),)
            return Vec(res)
        if isinstance(other, (int, float)):
            res = ()
            for x in self.ele:
                res = res + (round(x - other, 5),)
            return Vec(res)
        raise TypeError(f"Can't subtract Vec and {type(other)}")

    # Return a new vector with opposite values.
    def __neg__(self):
        res = ()
        for x in self.ele:
            res = res + (round(-1 * x, 5),)
        return Vec(res)

    # Use the add method for number + vector.
    def __radd__(self, other):
        return self.__add__(other)

    # Handle number - vector, or use the subtract method.
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            res = ()
            for x in self.ele:
                res = res + (round(other - x, 5),)
            return Vec(res)
        return self.__sub__(other)

    # Add and update this vector.
    def __iadd__(self, other):
        if not isinstance(other, (Vec, int, float)):
            raise TypeError(f"Can't add Vec and {type(other)}")
        vec = self.__add__(other)
        self.ele = vec.ele
        return self

    # Subtract and update this vector.
    def __isub__(self, other):
        if not isinstance(other, (Vec, int, float)):
            raise TypeError(f"Can't subtract Vec and {type(other)}")
        vec = self.__sub__(other)
        self.ele = vec.ele
        return self

    # Return a vector with n zeroes.
    @staticmethod
    def zeros(n: int):
        return Vec([0] * n)

    # Return a vector with n ones.
    @staticmethod
    def ones(n: int):
        return Vec([1] * n)

    # Return a vector with n random numbers from 0 up to 1.
    @staticmethod
    def uniform(n: int):
        return Vec([random.random() for _ in range(n)])

    # Return the length of the vector.
    def norm(self):
        sum_of_squares = 0
        for x in self.ele:
            sum_of_squares += x ** 2
        return math.sqrt(sum_of_squares)


if __name__ == "__main__":
    print("Q(6) copied Vec.py main test")
    vector = Vec((1, 2.345678, -3))
    other = Vec((4, 5, 6))
    print("vector:", vector)
    print("length:", len(vector))
    print("Vec + Vec:", vector + other)
    print("Vec + number:", vector + 2)
    print("number + Vec:", 2 + vector)
    print("number * Vec:", 2 * vector)
    print("Vec - Vec:", vector - other)
    print("Vec - number:", vector - 2)
    print("number - Vec:", 2 - vector)
    print("-Vec:", -vector)
    print("norm:", Vec((3, 4)).norm())
