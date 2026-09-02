from time import perf_counter
import numpy as np


sizes = (2000, 4000, 8000, 16000, 32000, 64000)

total_start = perf_counter()

for size in sizes:

    vector = np.array([float(i) for i in range(size)])
    other = np.array([1.0 for i in range(size)])

    print("\nVector length:", size)

    # __add__
    start = perf_counter()
    vector.__add__(other)
    end = perf_counter()
    print("__add__ Vec:", (end - start) * 1000, "ms")

    # __add__ number
    start = perf_counter()
    vector.__add__(2)
    end = perf_counter()
    print("__add__ number:", (end - start) * 1000, "ms")

    # __mul__
    start = perf_counter()
    vector.__mul__(2)
    end = perf_counter()
    print("__mul__:", (end - start) * 1000, "ms")

    # __sub__
    start = perf_counter()
    vector.__sub__(other)
    end = perf_counter()
    print("__sub__ Vec:", (end - start) * 1000, "ms")

    # __sub__ number
    start = perf_counter()
    vector.__sub__(2)
    end = perf_counter()
    print("__sub__ number:", (end - start) * 1000, "ms")

    # __neg__
    start = perf_counter()
    vector.__neg__()
    end = perf_counter()
    print("__neg__:", (end - start) * 1000, "ms")

    # zeros
    start = perf_counter()
    np.zeros(size)
    end = perf_counter()
    print("zeros:", (end - start) * 1000, "ms")

    # ones
    start = perf_counter()
    np.ones(size)
    end = perf_counter()
    print("ones:", (end - start) * 1000, "ms")

    # random
    start = perf_counter()
    np.random.random(size)
    end = perf_counter()
    print("random:", (end - start) * 1000, "ms")

    # norm
    start = perf_counter()
    np.linalg.norm(vector)
    end = perf_counter()
    print("norm:", (end - start) * 1000, "ms")


total_end = perf_counter()

print(
    "\nTotal time your PC took to complete this process:",
    total_end - total_start,
    "seconds"
)