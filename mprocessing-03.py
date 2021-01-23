from multiprocessing import Process

def language_func(language):
    print(language)


if __name__ == "__main__":
    languages = ['C', 'Python', 'Java', 'PHP']
    processes = []

    for language in languages:
        proc = Process(target=language_func, args=(language,))
        processes.append(proc)
        proc.start()

    for process in processes:
        process.join()