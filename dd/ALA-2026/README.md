# Custom vector class implementation 

A Python `Vec` class implemented using tuples. It supports vector addition, subtraction, scalar operations, in-place operations, negation, `len()`, `zeros()`, `ones()`, `uniform()`, and Euclidean norm.

## Files

- `Q(1to4)/Vec.py` — main implementation
- `Q(5)/test.py` — tests
- `Q(6)/performance.py` — custom performance benchmark
- `Q(7)/Vec_Colab_run.ipynb` — Colab benchmark run
- `Q(8)/perfo.py` — NumPy comparison

The benchmark uses Python's `time.perf_counter()` and tests vector sizes from 2,000 to 64,000 elements.

## Performance

- Local PC: completing all tests from vector size 2,000 to 64,000 took **58 seconds**
- Saved Google Colab run: **137.325091775 seconds**

Results can vary depending on the computer, Python version, available RAM, and runtime environment.



