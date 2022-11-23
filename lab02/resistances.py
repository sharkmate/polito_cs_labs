def main():
    
    
    r1 = int(input('insert the value of the first resistance'))
    r2 = int(input('insert the value of the second resistance'))
    r3 = int(input('insert the value of the third resistance'))
    r1_2 = ((r1*r2)/(r1+r2))
    r_tot = r1_2+r3
    print(f'the total resistance value is equal to {r_tot}')


if __name__ == '__main__':
    main()
