"""
The Drunkard’s Walk.
A drunkard in a grid of streets randomly picks one of four directions and stumbles to the next intersection,
then again randomly picks one of four directions, and so on.
You might think that on average the drunkard doesn’t move far because the choices cancel each other out,
but that is actually not the case.
Represent locations as integer pairs (x, y).
Implement the drunkard’s walk over 100 intersections, starting at (0,0), and print the ending location.
"""
import random
def main():
    x = 0
    y = 0
    for i in range(100):
        x += random.choice([1, (-1)])
        y += random.choice([1, (-1)])
    print(f"the final coordinates of the drunkyard are {x} and {y}")
if __name__ == "__main__":
    main()
