x_i = 1000 # Given x_0 value
a = 24693 # Multipler
c = 3517 # Increment
K = 2 ** 17 # Modulus

file = open('random_numbers.csv', 'a') # Open file to write with


for i in range(1, 10000):
    x_i = (a*x_i + c)%K
    file.write(str(x_i/K) + ','+"\n") 