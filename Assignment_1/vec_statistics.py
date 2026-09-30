from Vec import Vec as BaseVec
import math


class Vec(BaseVec):

    # Returns the mean of the vector
    def mean(self):
        if len(self) == 0:
            raise ValueError("Mean of an empty vector is undefined")

        total = 0
        for x in self.ele:
            total += x

        return total / len(self)

    # Returns vector representing the de-meaned vector
    def demean(self):
        mean_value = self.mean()

        result = ()
        for x in self.ele:
            result = result + (x - mean_value,)

        return Vec(result)

    # Returns the standard deviation of the vector
    def std(self):
        if len(self) == 0:
            raise ValueError("Standard deviation of an empty vector is undefined")

        de_meaned = self.demean()

        sum_of_squares = 0
        for x in de_meaned.ele:
            sum_of_squares += x ** 2

        return math.sqrt(sum_of_squares / len(self))