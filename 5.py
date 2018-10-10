#!/usr/bin/env python3

###
# Multiple functions, with a main organizing them
###

import csv
from models.flight import Flight

def main():
	fares_data = parse_file()	
	organize_by_destination_name(fares_data)

def parse_file():
	fares = []
	header_row = True
	with open('faresforbi.csv') as csvfile:
		fares_reader = csv.reader(csvfile)
		for row in fares_reader:
			if header_row:
				header_row = False
				continue
			fares.append(row)

	return fares

def organize_by_destination_name(fares_data):
	cities = {}
	for row in fares_data:
		flight = Flight(row)
		if(flight.arrival_city not in cities):
			cities[flight.arrival_city] = []

		cities[flight.arrival_city] = flight

	print("Number of unique arrival cities:", len(cities))
	print("Their names are:")

	for city in cities:
		print(city)

	return cities

if __name__== "__main__":
	main()
