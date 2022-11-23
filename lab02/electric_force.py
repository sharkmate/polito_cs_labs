"""
. According to Coulomb's law, the electric force (expressed in Newtons) between
two charged charged particles, respectively, Q1 and Q2, separated by a distance r, is
𝐹 =
𝑄1 𝑄2
4 𝜋 𝜀 𝑟
2
where 𝜀 =  8.854  × 10−12 Farad / meter. Write a program that calculates and shows on screen
the force relative to a pair of charged particles, allowing the user to choose the values Q1, Q2 (in
Coulomb) and r (in meters).
"""

EPSILON = 8.854*(10**(-12))
PI = 3.141592653589


def main():
    q1 = float(input("insert charge of the first particle"))
    q2 = float(input("insert charge of the second particle"))
    r = float(input("insert the distance in meters"))
    total_force = (q1*q2)/((r**2)*4*PI*EPSILON)
    print(f'the electric force between the two particles is {total_force}')


if __name__ == '__main__':
    main()
