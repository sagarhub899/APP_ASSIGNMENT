# Experiment No. 13
# Title: Study of Concurrency and Parallelism in Python
# Using Threading, Multiprocessing, Asyncio, and Logging

import asyncio
import logging
import multiprocessing
import threading
import time

logging.basicConfig(
    filename="exp1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Threading
def thread_task(n):
    print(f"Thread {n} started")
    logging.info(f"Thread {n} started")
    time.sleep(1)
    print(f"Thread {n} completed")

# Multiprocessing
def calculate_square(n):
    return n * n

# Async programming
async def async_task(n):
    print(f"Async task {n} started")
    await asyncio.sleep(1)
    print(f"Async task {n} completed")

async def run_async():
    await asyncio.gather(
        async_task(1),
        async_task(2),
        async_task(3)
    )

def main():
    print("--- THREADING ---")
    threads = [
        threading.Thread(target=thread_task, args=(i,))
        for i in range(1, 4)
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\n--- MULTIPROCESSING ---")
    with multiprocessing.Pool(3) as pool:
        print("Squares:", pool.map(calculate_square, [2, 3, 4]))

    print("\n--- ASYNCIO ---")
    asyncio.run(run_async())

    print("\n--- GIL COMPARISON ---")
    n = 1_000_000

    start = time.perf_counter()
    for _ in range(3):
        calculate_square(n)
    print("Sequential time:", round(time.perf_counter() - start, 4))

    start = time.perf_counter()
    with multiprocessing.Pool(3) as pool:
        pool.map(calculate_square, [n] * 3)
    print("Process time:", round(time.perf_counter() - start, 4))

    print("Check exp1.log for execution logs.")

if __name__ == "__main__":
    main()