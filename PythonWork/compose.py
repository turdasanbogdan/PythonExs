import profile 
import cars
from parse_dict import *

profile=profile.user_profile('ana','dana',varsta='19',scoala='CNAV')
car= cars.make_car('tesla', 'model s', parse(profile))