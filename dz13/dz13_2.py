import random
from random_words import RandomWords
import time

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(0, 5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

print("Int List:", int_list)
print("Float List:", float_list)
print("String List:", str_list)

def bubble_sort(data):
    length = len(data)
    for iIndex in range(length):
        swapped = False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex] > data[jIndex + 1]:
               data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
               swapped = True
        if not swapped:
            break

def avg_bubble(sort_list, n):
    time_list = []
    for i in range(n):
        start = time.time()
        bubble_sort(sort_list)
        time_list.append(time.time() - start)
    print("Average time of work:", sum(time_list) / n)

avg_bubble(int_list, 10)
avg_bubble(float_list, 10)
avg_bubble(str_list, 10)



