s=" "
ok=0
file= raw_input("file name")
for i in range(0,len(file)):
	if file[i] == '.':
		ok=1
	if ok == 1:
		s=s+file[i]	
print(s)		