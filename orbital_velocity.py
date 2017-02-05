import math

r = input("Earth Orbit: ")

R = 6.37 * (10 ** 6)    # Radius of Earth
G = 6.67 * (10 ** -11)  # Standard Gravitational Parameter
M = 5.97 * (10 ** 24)   # Mass of Earth
mu = G * M              # Mu of Earth (Gravitational Parameter * Earth's Mass)
r = R + r               # Radius of Earth + Radius of Orbit

v = math.sqrt(mu / r)   # Orbital Velocity for Entered Orbit

print("Orbital Velocity: " + str(v))
