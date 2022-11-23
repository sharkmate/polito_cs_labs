INT1 = 36
INT2 = 85


def main():
    sum_12 = INT1+INT2
    difference_12 = INT1-INT2
    product_12 = INT1*INT2
    average_value12 = (INT1+INT2)/2
    distance_12 = abs(INT1-INT2)
    max_value = max(INT1, INT2)
    min_value = min(INT1, INT2)
    print(f'the sum of the two numbers is {sum_12}')
    print(f' the difference of the two values is {difference_12}')
    print(f'the product oof the two numbers is {product_12}')
    print(f'the average value is{average_value12}')
    print(f'the distance between the two values is {distance_12}')
    print(f'the maximum value among the two numbers is{max_value}')
    print(f'the minimum value among the two numbers is{min_value}')


if __name__ == '__ main__':
    main()
