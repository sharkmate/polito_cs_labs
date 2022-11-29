"""
[1.1] Write a program reading a sequence of integer numbers (an empty string is the end of the sequence) and, after each input, executing and visualizing:

Partial sums of every number acquired; the program must visualize the result of the calculations after each input. As an example, if the input values are 1 7 2 9, the program shall visualize the partial sum of the numbers acquired after each input:
After the first input (1), the first acquired value: 1.
After the second input (7), the sum between the first and the second acquired values: 1 + 7 = 8.
After the third input (2), the sum between the first, the second, and the third acquired values: 1 + 7 + 2 = 10.
After the fourth input (9), the sum between the first, the second, the third, and the fourth values acquired: 1 + 7 + 2 + 9 = 19.
The minimum and the maximum values among the acquired ones.
How many acquired values are even, how many acquired values are odd.
"""

def main():
    part_sum = 0
    min_value = 100000000000
    max_value = 0
    even = 0
    odd = 0
    userinput = 0
    while userinput != " ":
        userinput = input("insert a number end with a space: ")
        if userinput != " ":
            if not userinput.isdigit():
                print("please ONLY numbers")
            nums = int(userinput)
            part_sum += nums
            if nums < min_value:
                min_value = nums
            if nums > max_value:
                max_value = nums
            if nums % 2 == 0:
                even += 1
            if nums % 2 == 1:
                odd += 1


    print(f" the partial sum is {part_sum}, the minimum value inserted is {min_value}, the maximum value inserted is {max_value} and you inserted a total of {even} even numbers and a total of {odd} odd numbers")
if __name__ == '__main__':
    main()
