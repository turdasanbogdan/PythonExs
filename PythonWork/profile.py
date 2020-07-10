from my_print import *

def user_profile(first_name, last_name, **info):
	profil={}
	profil['first_name']=first_name
	profil['last_name'] =last_name
	for key, val in info.items():
		profil[key]=val

	print_dict(profil)
	return profil

user_profile('ana','dana',varsta='19',scoala='CNAV')