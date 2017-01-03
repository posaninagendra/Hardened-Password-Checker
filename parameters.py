import random

# Global constants

# Large prime number
q = 5992830235524142758386850633773258681119

# h success iterations
h = 5

# Degree of random polynomial
m = None

# Random r
r = None

# Threshold of the features
t = 10

# Constant k
k = 2

# String literals
h_text = "HF\n"
h_file = "history.txt"
it_file = "instruction_table.txt"
out_file = "output.txt"
in_file = "input.txt"

# Constant integers
LOGIN_SUCCESS = 1
LOGIN_FAILED = 0
ENABLE_ERROR_CORRECTION = False

# Generates random r
def r_generator():
    global r
    r = random.getrandbits(160)
    with open("saved_r.txt", 'w') as f:
        f.write(str(r))
        f.close()