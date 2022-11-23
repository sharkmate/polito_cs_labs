"""
[06.2.2] Roman Numbers. Write a program that converts a Roman numeral, such as MCMLXXVIII, into its decimal representation. Tip: First, write a function that returns the numeric value of each individual letter, then use the following algorithm:

total = 0
s = string corresponding to the Roman numeral
Until s is empty
   If s has length 1, or the value of its first character is greater than or equal to the value of its second character
      Add the value of the first character of s to the total
      Remove the first character from s
   Otherwise
      difference = (value of the second character of s) – (value of the first character of s)
      Add the difference value to the total
      Remove the first two characters from s
      
"""



def convert_number():
    r_num = input("input a number in roman letters ")
    a_num = 0
    conv = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    if len(r_num) == 1:
        a_num += conv[r_num]
    else:
        for x in range(len(r_num)-1):
            if conv[r_num[x]] >= conv[r_num[x+1]]:
                a_num += conv[r_num[x]]
            else:
                a_num -= conv[r_num[x]]

    print(a_num+conv[r_num[-1]])



convert_number()
