from my_print import *

def make_car(producer, model, **info):
	car={}
	car['producer']=producer
	car['model']=model
	for key, val in info.items():
		car[key]= val
	print_dict(car)
	return car

make_car('tesla','model S', owner='Buhnici', kilos='10')		
