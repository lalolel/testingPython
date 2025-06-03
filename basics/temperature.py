# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# TURN UP THE TEMPERATURE

# Task 1: Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# Task 2: Test f_to_c with 100 Fahrenheit
f100_in_celsius = f_to_c(100)

# Task 3: Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Task 4: Test c_to_f with 0 Celsius
c0_in_fahrenheit = c_to_f(0)

# USE THE FORCE

# Task 5: Function to calculate force
def get_force(mass, acceleration):
    return mass * acceleration

# Task 6: Test get_force with train variables
train_force = get_force(train_mass, train_acceleration)
print(train_force)

# Task 7: Print force statement
print(f"The GE train supplies {train_force} Newtons of force.")

# Task 8: Function to calculate energy with default c value
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Task 9: Test get_energy with bomb_mass
bomb_energy = get_energy(bomb_mass)

# Task 10: Print energy statement
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# DO THE WORK

# Task 11: Function to calculate work
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    return force * distance

# Task 12: Test get_work with train variables
train_work = get_work(train_mass, train_acceleration, train_distance)

# Task 13: Print work statement
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")
