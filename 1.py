###
# Basic CSV Reading
###

import csv

with open('faresforbi.csv') as csvfile:
	fares_reader = csv.reader(csvfile)
	for row in fares_reader:
		print(','.join(row))
