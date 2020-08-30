import pprint
string="I am making good habits."
dict={}

for char in string:
	dict.setdefault(char,0)
	dict[char]=dict[char]+1
pprint.pprint(dict)