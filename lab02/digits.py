"""
Write a program that stores in a constant a positive five-digit integer (therefore
between 10000 and 99999), and displays the individual digits of which it is composed. For example,
having the number 16384, the program must display, on separate lines: 1 6 3 8 4. (p2.16)
"""
def main():
    
    
    num1 = int(input("input a five digit number"))
    print(num1//10000%10)
    print(num1//1000%10)
    print(num1//100%10)
    print(num1//10%10)
    print(num1%10)
    
    
if __name__ ==  '__main__':
    main()
