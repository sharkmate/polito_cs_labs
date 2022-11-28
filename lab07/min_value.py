"""Remove the minimum value. Write a

def remove_min(v)
function that removes the minimum value
 from a v list without using the min() function or the remove() method."""
import random

def main():
    rlist = []
    for i in range(100):
        rlist.append(random.randint(1, 100))
    min_value = 101
    for char in rlist:
        if char < min_value:
            min_value = char
    print(f"the list is {rlist}\nand the minimum value is {min_value}")

if __name__ == '__main__':
    main()


