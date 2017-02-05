import math

r = input("Orbit: ")

R = 6.37 * (10 ** 6)
G = 6.67 * (10 ** -11)
M = 5.97 * (10 ** 24)
mu = G * M
r = R + r

v = math.sqrt(mu / r)

print("Orbital Velocity: " + str(v))
