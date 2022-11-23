"""
Write a program that asks the user for an integer
 and then prints out all its factors.
 For example, when the user enters 150, the program should print

2

3

5

5


"""


def main():
    num = int(input("give me a number"))
    for i in range(2, num):
        while num % i == 0:
            print(str(i))
            num = num / i


if __name__ == "__main__":
    main()
