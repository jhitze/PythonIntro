#!/usr/bin/env python3

###
# Running as a function
###

import csv

def parse_file():
	with open('faresforbi.csv') as csvfile:
		fares_reader = csv.reader(csvfile)
		for row in fares_reader:
			print(','.join(row))

if __name__== "__main__":
	parse_file()
