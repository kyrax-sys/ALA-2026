from time import perf_counter
from Vec import Vec


sizes = (2000, 4000, 8000, 16000, 32000, 64000)

total_start = perf_counter()

for size in sizes:

    values = tuple(float(i) for i in range(size))
    other_values = tuple(1.0 for i in range(size))

    vector = Vec(values)
    other = Vec(other_values)

    print("\nVector length:", size)

    # __init__
    start = perf_counter()
    Vec(values)
    end = perf_counter()
    print("__init__:", (end - start) * 1000, "ms")

    # Vec + Vec
    start = perf_counter()
    vector + other
    end = perf_counter()
    print("Vec + Vec:", (end - start) * 1000, "ms")

    # Vec + number
    start = perf_counter()
    vector + 2
    end = perf_counter()
    print("Vec + number:", (end - start) * 1000, "ms")

    # number + Vec
    start = perf_counter()
    2 + vector
    end = perf_counter()
    print("number + Vec:", (end - start) * 1000, "ms")

    # number * Vec
    start = perf_counter()
    2 * vector
    end = perf_counter()
    print("number * Vec:", (end - start) * 1000, "ms")

    # Vec *= number
    start = perf_counter()
    temp = Vec(values)
    temp *= 2
    end = perf_counter()
    print("Vec *= number:", (end - start) * 1000, "ms")

    # Vec - Vec
    start = perf_counter()
    vector - other
    end = perf_counter()
    print("Vec - Vec:", (end - start) * 1000, "ms")

    # Vec - number
    start = perf_counter()
    vector - 2
    end = perf_counter()
    print("Vec - number:", (end - start) * 1000, "ms")

    # number - Vec
    start = perf_counter()
    2 - vector
    end = perf_counter()
    print("number - Vec:", (end - start) * 1000, "ms")

    # Vec -= Vec
    start = perf_counter()
    temp = Vec(values)
    temp -= other
    end = perf_counter()
    print("Vec -= Vec:", (end - start) * 1000, "ms")

    # Vec += Vec
    start = perf_counter()
    temp = Vec(values)
    temp += other
    end = perf_counter()
    print("Vec += Vec:", (end - start) * 1000, "ms")

    # Vec += number
    start = perf_counter()
    temp = Vec(values)
    temp += 2
    end = perf_counter()
    print("Vec += number:", (end - start) * 1000, "ms")

    # Vec -= number
    start = perf_counter()
    temp = Vec(values)
    temp -= 2
    end = perf_counter()
    print("Vec -= number:", (end - start) * 1000, "ms")

    # -Vec
    start = perf_counter()
    -vector
    end = perf_counter()
    print("-Vec:", (end - start) * 1000, "ms")

    # __repr__
    start = perf_counter()
    repr(vector)
    end = perf_counter()
    print("__repr__:", (end - start) * 1000, "ms")

    # __len__
    start = perf_counter()
    len(vector)
    end = perf_counter()
    print("__len__:", (end - start) * 1000, "ms")

    # zeros
    start = perf_counter()
    Vec.zeros(size)
    end = perf_counter()
    print("zeros:", (end - start) * 1000, "ms")

    # ones
    start = perf_counter()
    Vec.ones(size)
    end = perf_counter()
    print("ones:", (end - start) * 1000, "ms")

    # uniform
    start = perf_counter()
    Vec.uniform(size)
    end = perf_counter()
    print("uniform:", (end - start) * 1000, "ms")

    # norm
    start = perf_counter()
    vector.norm()
    end = perf_counter()
    print("norm:", (end - start) * 1000, "ms")


total_end = perf_counter()

print(
    "\nTotal time your PC took to complete this process:",
    total_end - total_start,
    "seconds"
)