import queue
import sys
import multiprocessing

q = queue.Queue()
word1 = "Ludwigshafen"
word2 = "Mannheim"

def put(word):

    q_list = list()

    for item in word:
        q.put(item)

        q_list.append(item)
    
    print(q_list)
    while True:
        if q.empty():
            sys.exit()
        item = q.get()
        q.task_done()
        process_name = multiprocessing.current_process().name
        print(f"Letter {item} is gone by {process_name}")


processes = []

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=put, args=(word1,))
    process2 = multiprocessing.Process(target=put, args=(word2,))
    processes.append(process1)
    processes.append(process2)
    
    for process in processes:
        process.start()
        process.join()