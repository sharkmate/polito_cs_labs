"""
 Format the output of exercise 02.1.1 so that descriptions and numbers are
aligned vertically, for example:


Sum:        45
Difference: -5
"""
INT1 = 36
INT2 = 78


def main():
    sum_12 = INT1+INT2
    difference_12 = INT1-INT2
    product_12 = INT1*INT2
    average_value12 = (INT1+INT2)/2
    distance_12 = abs(INT1-INT2)
    max_value = max(INT1, INT2)
    min_value = min(INT1, INT2)
    print(f'{"sum:":<25}{sum_12}')
    print(f'{"difference:":<25}{difference_12}')
    print(f'{"product:":<25} {product_12}')
    print(f'{"value:":<25} {average_value12}')
    print(f'{"distance:":<25} {distance_12}')
    print(f'{"maximum value:":<25} {max_value}')
    print(f'{"minimum value:":<25} {min_value}')


if __name__ == '__main__':
    main()
