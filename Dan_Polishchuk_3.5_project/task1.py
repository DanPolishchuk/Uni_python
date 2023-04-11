import queue
import sys
import multiprocessing

q = queue.Queue()
word1 = "Ludwigshafen"
word2 = "Mannheim"

def put(word):                                         # A function that puts letters of a word into the queue
                                                       
    q_list = list()                                    # Create a list to store elements added to the queue

    for item in word:                                  # Iterate through the letters of the word and put them into the queue
        q.put(item)

        q_list.append(item)
    
    print(q_list)                                      # Print the list of items that were added to the queue
    while True:                                        # Continuously get items from the queue and print them until the queue is empty
        if q.empty():
            sys.exit()
        item = q.get()
        q.task_done()
        process_name = multiprocessing.current_process().name
        print(f"Letter {item} is gone by {process_name}")


processes = []

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=put, args=(word1,))                     # Create two processes and add them to a list
    process2 = multiprocessing.Process(target=put, args=(word2,))                     
    processes.append(process1)
    processes.append(process2)
    
    for process in processes:                                                         # Start each process and wait for them to finish
        process.start()                                                               # Wait for each process to finish before continuing
        process.join()