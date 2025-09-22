import re
mystr = "anshu isssss aaaaaaaiiiii 22209-1911 gooodddddd girrrrllllllll Fax Faxa and sheeee iiisss smmmaarrtt Tata fass  fadm gghhadm  admi  ai ai t t admjj adddadm"

patt = re.compile(r'fass')
patt = re.compile(r'.')  #Any character , Prints all characters.
patt = re.compile(r'.adm')
patt = re.compile(r'^adm') # Starts with
patt = re.compile(r'adm$') #ends with
patt = re.compile(r'ai*') #zero or more occurrences
patt = re.compile(r'ai+') #one or more occurrences
patt = re.compile(r'ai{2}') # {} Exactly the specified number of occurrences eg : aii
patt = re.compile(r'(ai){2}') #search aiai 
patt = re.compile(r'ai{1} | t') # Either or 

#Special Sequences

patt = re.compile(r'\ATata')  # Returns a match if specified char are at the beg of string.
patt = re.compile(r'\bFax') #Returns a match where specified char are at beg or end.
patt = re.compile(r'\d{5}-\d{4}') #\d returns a match where the string contains digits.


matches = patt.finditer(mystr)
for match in matches:
    print(match)

