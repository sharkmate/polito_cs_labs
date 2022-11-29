"""
Buffe.r
Write the pseudocode for an algorithm that, given a list of defined length,
moves the elements "forward" one position (thus increasing their index by one unit),
and moves the element at the last position to the first position.
For example, the list 1 7 9 3 0 4, after this operation,
becomes the list: 4 1 7 9 3 0.
Write a program implementing the above described algorithm.
"""
#using two different methods one with list operators one with a for cycle

def buffer1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums.insert(0, nums[-1])
    nums.pop(-1)
    return nums
def buffer2():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_list = [nums[-1]]
    for el in nums[:-1]:
        new_list.append(el)
    return new_list
print(buffer1(), buffer2())



