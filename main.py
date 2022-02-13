from sympy import *
import os

os.system('clear')
previous = 1
count = 0
while True:
	count += 1
	current = nextprime(previous)
	previous = current
	if count % 13553 == 0:
		os.system('clear')
		print(f'Count: {count:,}\nNumber: {current:,}')