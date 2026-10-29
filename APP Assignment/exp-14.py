# Experiment No.14
# Title: Implement Logging in Python
# Using Logging Levels, File and Console Logging,
# Exception Handling, and Multithreading

import logging
import threading
import time

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(threadName)s - %(message)s",
    handlers=[
        logging.FileHandler("exp2.log", mode="w"),
        logging.StreamHandler()
    ],
    force=True
)

def perform_task(task_id):
    logging.info(f"Task {task_id} started")
    time.sleep(0.5)

    try:
        if task_id == 2:
            raise ValueError("Example error occurred")

        logging.info(f"Task {task_id} completed successfully")

    except Exception:
        logging.exception(f"Task {task_id} failed")

def main():
    print("--- LOGGING LEVELS ---")

    logging.debug("Debug message")
    logging.info("Information message")
    logging.warning("Warning message")
    logging.error("Error message")
    logging.critical("Critical message")

    print("\n--- EXCEPTION LOGGING ---")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logging.exception("Division by zero occurred")

    print("\n--- MULTITHREADING WITH LOGGING ---")
    threads = []

    for i in range(1, 4):
        t = threading.Thread(
            target=perform_task,
            args=(i,),
            name=f"Worker-{i}"
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nCheck exp2.log for complete logs.")

if __name__ == "__main__":
    main()


