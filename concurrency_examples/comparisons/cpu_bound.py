import threading
import multiprocessing
import math
from utils.decorators import time_it


# 2. CPU-Bound Computation
def compute_factorial(n):
    """Computes factorial (CPU-intensive)."""
    return math.factorial(n)


# 3. Single-threaded Execution
@time_it
def run_single_thread(numbers):
    return [compute_factorial(n) for n in numbers]


# 4. Multithreading Execution (Ineffective due to GIL)
@time_it
def run_multithreading(numbers):
    threads = []
    results = []

    def worker(n):
        results.append(compute_factorial(n))

    for num in numbers:
        thread = threading.Thread(target=worker, args=(num,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


# 5. Multiprocessing Execution (Effective for CPU-bound tasks)
@time_it
def run_multiprocessing(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(compute_factorial, numbers)
    return results


# 6. Execution
if __name__ == "__main__":
    test_numbers = [50000] * 100  # Large numbers for CPU-intensive calculations
    print("=== CPU-BOUND TASKS ===")
    run_single_thread(test_numbers)
    run_multithreading(test_numbers)
    run_multiprocessing(test_numbers)
