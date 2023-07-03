import time

def start_stopwatch():
    start_time = time.time()
    print("Stopwatch started.")

    input("Press Enter to stop the stopwatch.")

    elapsed_time = time.time() - start_time
    print("Elapsed time: {:.2f} seconds".format(elapsed_time))

def main():
    input("Press Enter to start the stopwatch.")
    start_stopwatch()

if __name__ == "__main__":
    main()
