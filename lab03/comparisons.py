"""

[1.1] For each of the following pairs of values, perform an equality test, assign the result to a variable, and display it. Try to predict what the result of each test will be.

1, 1
1, 1.0
2.0, sqrt(4)
'1', 1
'hello', 'Hello'
"""
import math


def main():
    print(1 == 1)
    print(1 == 1.0)
    print(2.0 == math.sqrt(4))
    print("1"== 1)
    print("hello" == "Hello")


if __name__ == "__main__":
    main()