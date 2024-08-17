from threading import Thread, Lock
import time

"""A very, very, very long document"""
current = "lorem ipsum"
lorem = open("threading practice 1/lorem.txt", "r")

content = lorem.read()
content = content.replace(".", "")
content = content.split()

def total_list_items(list, lock):
    with lock:
        amount = len(list)
        print(f"The total amount of items in the pharagraph is: {amount}\n")
        time.sleep(0.1)

def all_list_items(list, lock):
    with lock:
        ordered = list.sort()
        print(f"The sorted version of these words is: {ordered}\n")
        time.sleep(0.1)

def largest_words(list, lock):
    with lock:
        large_words = []
        for item in list:
            if (len(list) == 0) or (len(item) == len(list[-1])):
                list.append(item)
            elif len(item) > len(list[-1]):
                large_words[-1] = item
        print(f"The largest words are: {large_words}\n")
        time.sleep(0.1)

if __name__ == "__main__":
    lock = Lock()
    print("This program uses threading to calculate different things of different pharagraphs.\n")
    while True:
        user_input = input(f"This will play information about {current}. Type q to quit, otherwise, don't do anything.: ")
        if user_input.lower() == "q":
            break

        thread1 = Thread(target=total_list_items, args=(lock, content))
        thread2 = Thread(target=all_list_items, args=(lock, content))
        thread3 = Thread(target=largest_words, args=(lock, content))

        thread1.start()
        thread2.start()
        thread3.start()

        thread1.join()
        thread2.join()
        thread3.join()

        print("Please type in a pharagraph that you want to be inspected below:\n")
        lorem.close()
        content = input()
        content = content.replace(".", "")
        content = content.split()
        current = input("What is the name of this pharagraph?:")