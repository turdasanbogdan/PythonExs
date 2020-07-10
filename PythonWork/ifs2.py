users=['Alinus', 'Pedro Orteghia', 'Danzo', 'admin']
# if users:
#      for user in users:
# 	      if user == 'admin':
# 	           print("Hello boss, would you like to see a report")
# 	      else:
# 	           print("Hello "+ user.title() + ", nice to see you")   
# else: 
#     print("We need users")	           

new_users=['Alinus', 'Calu', 'Ciuperca', 'DANZO']

for new_user in new_users :
	try:	
		for user in users :
			if new_user.lower() == user.lower() :
		    		raise StopIteration
		 
	except StopIteration:
       			print("Username already taken, try new one")
	else:        
       			print("Welcome " + new_user.lower().title())		  
print("Done")