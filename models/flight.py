class Flight:
	def __init__(self, row):
		self.year = row[0]
		self.month = row[1]
		self.departure_city = row[3]
		self.arrival_city = row[4]
		self.cost = row[7]