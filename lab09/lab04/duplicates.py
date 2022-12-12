def user_input():
    num = ""
    while num != " ":
        num += input("insert a series of numbers, terminate w/ empty line")
    return num

def main():
    print(user_input())
if __name__ == '__main__':
    main()