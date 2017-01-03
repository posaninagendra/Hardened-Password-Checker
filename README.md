# Hardened Password Checker
A high secure password checker using the key strokes of the user as input along with the password. 

The goal of this project is to implement a more secure authentication scheme by capturing the key strokes values as features using the techniques described in the paper [password hardening](http://link.springer.com/article/10.1007/s102070100006). 

### 0. Dependencies
Following python dependency packages need to be installed on the machine to run the program. 
* pycrypto
* mpmath
* math
* random

### 1. Parameters
* Number of success login attempts saved in history  le:  h = 5
* Feature threshold:  t = 10
* Parameter:  k = 2

### 2. Running Instructions
To run the python server script, LINUX operating system is preferred.  The script expects an input file named "input:txt" with N login attempts of password and feature values having '\n' as delimiter.  To enable error correction set the flag ENABLE_ERROR_CORRECTION to True in parameters.py by  default  it  is  set  to False.  The program creates "output.txt" with series of 1's and 0's where 1 = successful login and 0 = login failed, along with this  le it also creates instruction table.txt, saved txt and history.txt files. 

_This project is part of the course work CS 6238 at Georgia Tech_
