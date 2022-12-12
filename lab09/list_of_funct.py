
list_funct = [1, 2, 3, 4, 5, 6, 7, 8]

def swap(b: list):
    b.append(b[0])
    b.insert(0, b[-2])
    b.pop(1)
    b.pop(-2)
    return b




def shift():
    list_funct.insert(0, list_funct[-1])
    list_funct.pop(-1)
    return list_funct


def replace_even(giovanni: list):
    print(giovanni)
    for index, element in enumerate(giovanni):
        if element % 2 == 0:
            giovanni.insert(giovanni[index], 0)
            giovanni.pop(giovanni[index-1])

    return giovanni

def replace_neighbour(a: list):
    print(a)
    for index, element in enumerate(a):
        if index != 0 and index != -1:
            if a[index-1] < a[index+1]:
                a.insert(index, a[index+1])
                a.pop(index-1)
                if IndexError:
                    break
            else:
                a.insert(index, a[index-1])
                a.pop(index-1)
    print(a)
replace_neighbour(list_funct)




