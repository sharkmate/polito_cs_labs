"""
Write a program that reads all the lines in a text file input.txt,
reverses their order, and writes them to another file output.txt.
"""
def main():
    with open("input.txt") as input_:
        lines = input_.readlines()
    with open("output.txt", "x") as output:
        for line in lines[::-1]:
            if line==lines[-1]:
                output.write(line)
                output.write("\n")
            else:
                output.write(line)

if __name__ == '__main__':
    main()
