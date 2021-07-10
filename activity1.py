import numpy as np

def tryTriangle(var1, var2, var3):
    a = np.sqrt(var1**2 + var2**2)  # a is the hypotenuse
    if a == var3: return print('This triangle IS a right triangle!')
    else: return print('This triangle IS NOT a right triangle!')


hypotenuse = float(input("Value of the hypotenuse: "))
adjacent = float(input("Value of the adjacent: "))
opposite = float(input("Value of the opposite: "))

tryTriangle(adjacent, opposite, hypotenuse)

