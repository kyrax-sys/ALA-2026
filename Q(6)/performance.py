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

    # __add__ Vec
    start = perf_counter()
    vector.__add__(other)
    end = perf_counter()
    print("__add__ Vec:", (end - start) * 1000, "ms")

    # __add__ number
    start = perf_counter()
    vector.__add__(2)
    end = perf_counter()
    print("__add__ number:", (end - start) * 1000, "ms")

    # __radd__
    start = perf_counter()
    vector.__radd__(2)
    end = perf_counter()
    print("__radd__:", (end - start) * 1000, "ms")

    # __rmul__
    start = perf_counter()
    vector.__rmul__(2)
    end = perf_counter()
    print("__rmul__:", (end - start) * 1000, "ms")

    # __imul__
    start = perf_counter()
    Vec(values).__imul__(2)
    end = perf_counter()
    print("__imul__:", (end - start) * 1000, "ms")

    # __sub__ Vec
    start = perf_counter()
    vector.__sub__(other)
    end = perf_counter()
    print("__sub__ Vec:", (end - start) * 1000, "ms")

    # __sub__ number
    start = perf_counter()
    vector.__sub__(2)
    end = perf_counter()
    print("__sub__ number:", (end - start) * 1000, "ms")

    # __rsub__
    start = perf_counter()
    vector.__rsub__(2)
    end = perf_counter()
    print("__rsub__:", (end - start) * 1000, "ms")

    # __isub__
    start = perf_counter()
    Vec(values).__isub__(other)
    end = perf_counter()
    print("__isub__:", (end - start) * 1000, "ms")

    # __iadd__
    start = perf_counter()
    Vec(values).__iadd__(other)
    end = perf_counter()
    print("__iadd__:", (end - start) * 1000, "ms")

    # __neg__
    start = perf_counter()
    vector.__neg__()
    end = perf_counter()
    print("__neg__:", (end - start) * 1000, "ms")

    # __repr__
    start = perf_counter()
    vector.__repr__()
    end = perf_counter()
    print("__repr__:", (end - start) * 1000, "ms")

    # __len__
    start = perf_counter()
    vector.__len__()
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
print("\nTotal time your pc took to complete this process:", total_end - total_start, "seconds")