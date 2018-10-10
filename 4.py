#!/usr/bin/env python3

###
# Multiple functions, returning data, parameters
###

import csv

def main():
	fares_data = parse_file()
	print_destination_names(fares_data)

def parse_file():
	fares = []

	with open('faresforbi.csv') as csvfile:
		fares_reader = csv.reader(csvfile)
		for row in fares_reader:
			fares.append(row)

	return fares

def print_destination_names(fares_data):
	for row in fares_data:
		if row is not None:
			print(row[4])

if __name__== "__main__":
	main()
