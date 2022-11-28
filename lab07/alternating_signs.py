"""
Sum with alternating signs.
Write a program that receives as input a sequence of integers (terminated by an empty line),
and that calculates the alternating sum of its elements.
For example, if the program reads the data 1 4 9 16 9 7 4 9 11,
it must calculate and display 1 - 4 + 9 - 16 + 9 - 7 + 4 - 9 + 11 = –2.
"""


def main():
    nums = 0
    nums_list = []
    result = 0
    while not nums == " ":
        nums = (input("insert a number, stop with a white space "))
        nums_list.append(nums)
        if ValueError:
            break
    nums_list.pop(-1)
    for i in nums_list[1::2]:
        result += int(i)
    for j in nums_list[0::2]:
        result -= int(j)

    print(nums_list, result)


if __name__ == "__main__":
    main()
