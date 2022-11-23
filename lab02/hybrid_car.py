"""
Writing the pseudocode and its Python program that helps a person decide
whether or not to buy a hybrid car. The inputs of the program should be:
I. the cost of a new car;
II. the estimate of the kilometers traveled in a year;
III. The estimate of the cost of fuel;
IV. Efficiency in kilometers per liter;
V. The estimate of the resale value of the used car after 5 years.
Calculate the total cost of ownership of the car for 5 years (for simplicity, do not take into account
the cost of financing). To provide input to the program, search the Web for realistic prices and
consumption for two alternatives for buying a new car in the same price range: a hybrid model or
and a gasoline. Run the program twice to compare the two alternatives, considering the current fuel
price and the forecast of traveling 30,000 kilometers per year. (2.10 pm)
"""


def main():
    
    
    cost = int(input("cost of the car?"))
    km_per_yr = 30_000
    fuel_per_l = float(input('how much does a liter of fuel cost?'))
    km_per_l = int(input('how many kms can the car travel with one liter of fuel?'))
    resell_value = int(input('for how much could you sell the car after 5 years?'))
    fuel_tot = ((km_per_yr*5)/km_per_l)*fuel_per_l
    print(f'the total cost of the car for five years is {(cost+fuel_tot-resell_value)}')

    
if __name__ == '__main__':
    main()
