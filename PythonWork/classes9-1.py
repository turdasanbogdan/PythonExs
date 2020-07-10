class Restaurant():

	def __init__(self, name, tip):
		self.name=name
		self.cousine_type=tip
	def open_restaurant(self):
		print("Restaurant: " + self.name + " is opened now" )
		
restaurant= Restaurant('Gucino','Italian')
restaurant.open_restaurant()