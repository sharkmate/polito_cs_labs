""" List of random numbers. Write a program that initializes a list with ten random integers between 1 and 100 and then displays, on four successive lines:

I. All elements of even index;
II. All elements of even value;
III. All elements in reverse order;
IV. The first and the last element.
"""


import random



def main():

    rlist = []
    for i in range(100):
        rlist.append(random.randint(1,100))
    even_list = []
    for n in range(100):
        if n%2 == 0:
            even_list.append(rlist[n])
    even_value = []
    for char in rlist:
        if char%2 == 0:
            even_value.append(char)
    reverse = []
    for n in range(1, 101):
        reverse.append(rlist[-n])
    print(f"the list of random numbers is {rlist}")
    print(f"the numbers  with even indexes are {even_list}")
    print(f"the even values in the list are {even_value}")
    print(f"the reversed list is {reverse}")
    print(f" the first number in the list is {rlist[0]}, the last number is {rlist[-1]}")





if __name__ == '__main__':
    main()


