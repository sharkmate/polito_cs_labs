def user_input():
    numbers = ""
    num = ""
    while num != " ":
        num = input("insert a series of numbers, terminate w/ empty line")
        numbers += num
    numbers = int(numbers.rstrip())
    return numbers

def main():
    print(user_input())
if __name__ == '__main__':
    main()