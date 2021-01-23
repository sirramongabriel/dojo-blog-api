from multiprocessing import Process

def process_function():
    print('Hello World')

if __name__ == "__main__":
    proc = Process(target=process_function)
    proc.start()
    proc.join()