def format_name(first,last, middle=''):
  if not middle:
  	return first+' '+last
  else:
  	return first+' '+middle+' '+last

print(format_name("ana", "alina","adad"))  		