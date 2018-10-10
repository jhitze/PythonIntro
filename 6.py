#!/usr/bin/env python3

###
# Switch prints for logging
###

import csv
import logging
from models.flight import Flight

logger = logging.getLogger('fares')

def main():
	setup_logging()
	logger.info("Starting processing.")
	fares_data = parse_file()
	# print_destination_names(fares_data)
	organize_by_destination_name(fares_data)
	logger.info("Finished processing.")

def setup_logging():
	logger.setLevel(logging.DEBUG) 
	# create console handler and set level to debug
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)

	# create formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

	# add formatter to ch
	ch.setFormatter(formatter)

	# add ch to logger
	logger.addHandler(ch)

def parse_file():
	logger.debug("Going to parse file...")
	fares = []
	header_row = True
	with open('faresforbi.csv') as csvfile:
		fares_reader = csv.reader(csvfile)
		for row in fares_reader:
			if header_row:
				header_row = False
				continue
			fares.append(row)

	logger.debug("Finished parsing file.")
	return fares

def organize_by_destination_name(fares_data):
	cities = {}
	for row in fares_data:
		flight = Flight(row)
		if(flight.arrival_city not in cities):
			cities[flight.arrival_city] = []

		cities[flight.arrival_city] = flight


	logger.info("Number of unique arrival cities: {}".format( len(cities)))
	logger.debug("Their names are: {}".format(", ".join(cities)))

	return cities

if __name__== "__main__":
	main()
