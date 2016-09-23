hashedString = int(input("Enter the : "))
print "The hash " +str(hashedString)

# hashedString =	680131659347
# print "The string is " +str(hashedString)
letters = "acdegilmnoprstuw"
# print len(letters)
i=hashedString
decodedString=""
# print letters[0]
# print letters[15]

try :
	'''Looping till  length of letters-1'''
	while i> 15 :
		h=i%37
		# print h
		decodedString=letters[h]+decodedString
		i=i-h
		i=i/37

	print "The reverse hash of "+ str(hashedString) +" is "+decodedString

except IndexError:
	print "The string index is out of range "

except:
	print "There is a bug in the program"
