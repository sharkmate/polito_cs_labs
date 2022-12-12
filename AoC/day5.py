def show_stacks(stacks: list):
    print("\n\n stacks: \n ")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

def main():
    with open("scratch5") as text:
        stack_lines, instructions = (i.splitlines() for i in text.read().strip("\n").split("\n\n"))
    stacks = {int(digit) for digit in stack_lines[-1].replace(" ", "")}
    print(stacks)
    show_stacks(stacks)
if __name__ == "__main__":
    main()
