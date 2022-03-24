import math


'''Helper functions to be used in realization'''
def get_rand(file_reader): # helper function to get calculated random values
    return float(file_reader.readline().replace(',', ''))

def X_realization(rand_nums_file):
    return -12*math.log(1 - get_rand(rand_nums_file)) # Finds corresponding amount of time to probability for case customer is available


'''Recursive process for simulating call'''
def W_realization(rand_nums_file, num_calls=1):
    if num_calls==5: # Recursive Base Case , caller is called 4 complete times and the trial is terminated
        return 0
    u_i = get_rand(rand_nums_file) # Get Random Number for trial

    if 0 <= u_i <= .2:
        return 10 + W_realization(rand_nums_file, num_calls+1) # Line is Busy
    if .2 < u_i <= .5:
        return 32 + W_realization(rand_nums_file, num_calls+1) # Customer is unavailable
    if .5 < u_i <= 1:
        X = X_realization(rand_nums_file)
        if (X > 25): 
            return 32 + W_realization(rand_nums_file, num_calls +1) # Customer cannot reach the phone in time
        else:
            return X + 7 # Customer is reached and the trial is terminated



################ Simulation ######################
rand_nums_file = open('random_numbers.csv')
data_file = open('output.csv', 'w')

for i in range(1000):
    x_i = W_realization(rand_nums_file)
    data_file.write(str(x_i) + ',' + '\n')


    

    


