# Code to calculate the time taken by the process in python

# Import the timer library
import timeit
import time

# Record the starting time of the process
start_time=timeit.default_timer()

# Carry out the required processing here
# A dummy sleep is added
time.sleep(3)

# Record the ending time of the process
end_time=timeit.default_timer()

#Get the elapsed time in seconds
total_time=end_time-start_time
print total_time 
