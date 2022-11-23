"""
Geometric solids. Write functions:

def sphere_volume(r)
def sphere_surface(r)
def cylinder_volume(r, h)
def cylinder_surface(r, h)
def cone_volume(r, h)
def cone_surface(r, h)
Such functions are devoted to calculate the volume and surface area of a sphere of radius r,
a cylinder with a circular
base of radius r and height h, and a cone with a circular base with radius r and height h.
Then write a program that asks the user to enter the values r and h,
then the program calls the six functions and display the output results. [P5.9]
"""

PI = float(3.141592653589)
import math

def sphere_volume(r):
    volume = (4 / 3) * PI * r ** 3
    return volume


print(sphere_volume(5))


def sphere_surface(r):
    surface = 4 * PI * r ** 2
    return surface


print(sphere_surface(5))


def cylinder_volume(r, h):
    area_base = PI * r ** 2
    volume = area_base * h
    return volume


print(cylinder_volume(3, 10))


def cylinder_surface(r, h):
    area_base = PI * r ** 2
    area_square = 2*PI*r*h
    cylinder_surface = area_base + area_square
    return cylinder_surface


print(cylinder_surface(5,3))


def cone_volume(r, h):
    area_base = PI * r ** 2
    volume = (area_base * h)/3
    return volume

print(cone_volume(4, 6))


def cone_surface(r, h):
    area_base = PI * r ** 2
    area_trg = PI*r*(math.sqrt(r**2+h**2))
    cone_surface = area_base + area_trg
    return cone_surface

print(cone_surface(3, 7))


