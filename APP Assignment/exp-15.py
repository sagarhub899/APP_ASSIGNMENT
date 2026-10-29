# Title: Study of Memory Management in Python
# Using Memory Profiling, Garbage Collection,
# Reference Cycles, and Memory Allocation Tracking

import gc
import logging
import tracemalloc

logging.basicConfig(
    filename="exp3.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Node:
    def __init__(self):
        self.reference = None

def show_memory(label):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{label}: Current={current} bytes, Peak={peak} bytes")
    logging.info(
        "%s: Current=%s bytes, Peak=%s bytes",
        label, current, peak
    )

def main():
    print("--- MEMORY PROFILING ---")
    tracemalloc.start()

    show_memory("Before allocation")

    data = [i for i in range(100000)]
    show_memory("After allocation")

    print("\n--- REFERENCE CYCLE ---")
    a = Node()
    b = Node()

    a.reference = b
    b.reference = a

    del a
    del b

    print("GC thresholds:", gc.get_threshold())
    print("GC counters:", gc.get_count())

    collected = gc.collect()
    print("Objects collected:", collected)

    logging.info("Objects collected: %s", collected)

    print("\n--- MEMORY AFTER DELETION ---")
    del data
    show_memory("After deleting list")

    print("\n--- MEMORY ALLOCATION DETAILS ---")
    snapshot = tracemalloc.take_snapshot()

    for stat in snapshot.statistics("lineno")[:5]:
        print(stat)

    tracemalloc.stop()
    print("\nCheck exp3.log for memory logs.")

if __name__ == "__main__":
    main()