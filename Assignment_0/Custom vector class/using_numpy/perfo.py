from time import perf_counter
import numpy as np


sizes = (2000, 4000, 8000, 16000, 32000, 64000)

total_start = perf_counter()

for size in sizes:

    vector = np.array([float(i) for i in range(size)])
    other = np.array([1.0 for i in range(size)])

    print("\nVector length:", size)

    # NumPy Vec + Vec
    start = perf_counter()
    vector + other
    end = perf_counter()
    print("Vec + Vec:", (end - start) * 1000, "ms")


    # NumPy number * Vec
    start = perf_counter()
    2 * vector
    end = perf_counter()
    print("number * Vec:", (end - start) * 1000, "ms")

    # NumPy Vec - Vec
    start = perf_counter()
    vector - other
    end = perf_counter()
    print("Vec - Vec:", (end - start) * 1000, "ms")


    # NumPy negative
    start = perf_counter()
    -vector
    end = perf_counter()
    print("-Vec:", (end - start) * 1000, "ms")

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
    print("uniform:", (end - start) * 1000, "ms")

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