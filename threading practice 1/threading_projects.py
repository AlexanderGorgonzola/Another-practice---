from multiprocessing import Process
import time

"""A very, very, very long document"""
pharagraph = open("threading practice 1/lorem_ipsum.txt", "r")

content = pharagraph.read()
content = content.replace(".", "")
content = content.replace("?", "")
content = content.replace("!", "")
content = content.replace(",", "")
content = content.split()
pharagraph.close()
def total_list_items(list):
    amount = len(list)
    print(f"\nThe total amount of items in the pharagraph is: {amount}\n")
    time.sleep(0.1)

def all_list_items(list):
    list.sort()
    print(f"The sorted version of these words is: {list}\n")
    time.sleep(0.1)

def largest_words(list):
    large_words = []
    for item in list:
        if len(item) >= 11:
            large_words.append(item)
    if len(large_words) > 0:
        print(f"The large word(s) in this pharagraph are: {large_words}\n")
    else:
        print("Their where no long words in this pharagraph :(")
    time.sleep(0.1)

if __name__ == "__main__":
    print("This program uses multiple processes to calculate different things of different pharagraphs.\n")
    while True:
        user_input = input(f"This will play information about your pharagraph. Type q to quit, otherwise, don't do anything.: ")
        if user_input.lower() == "q":
            break

        process1 = Process(target=total_list_items, args=(content,))
        process2 = Process(target=all_list_items, args=(content,))
        process3 = Process(target=largest_words, args=(content,))

        process1.start()
        process2.start()
        process3.start()

        process1.join()
        process2.join()
        process3.join()

        print("Please type in a pharagraph that you want to be inspected below:\n")
        pharagraph = open("threading practice 1/lorem_ipsum.txt", "w")
        content = input()
        pharagraph.write(content)
        pharagraph.close()
        content = content.replace(".", "")
        content = content.split()