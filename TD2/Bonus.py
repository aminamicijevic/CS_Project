import math

powers = [2**i for i in range(20)]
print(powers)

approximations = [round(math.pi, i) for i in range(1, 15)]
print(approximations)

xpoints = [1, 2, -1]
ypoints = [8, 4, 3, 0]
zpoints = [0, -1]

points = [(x, y, z) for x in xpoints for y in ypoints for z in zpoints]
print(points)
