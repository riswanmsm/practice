#!/usr/bin/env python

""" module.py - an example of a Python module """

__counter = 0

def sum_list(the_list):
	global __counter
	__counter += 1
	the_sum = 0
	for el in the_list:
		the_sum += el
	return the_sum

def prod_list(the_list):
	global __counter
	__counter += 1
	prod = 1
	for el in the_list:
		prod *= el
	return prod


if __name__ == "__main__":
	print("I prefer to be a module")
	my_list = [i+1 for i in range(5)]
	print(sum_list(my_list) == 15)
	print(prod_list(my_list) == 120)


