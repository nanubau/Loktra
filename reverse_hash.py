def reverse_hash(hashedInt):
	try :
		letters = "acdegilmnoprstuw"
		# print len(letters)
		i=hashedInt
		decodedString=""
		'''Looping till  length of letters-1'''
		while i> 15 :
			h=i%37
			# print h
			decodedString=letters[h]+decodedString
			i=i-h
			i=i/37

		print "The reverse hash of "+ str(hashedInt) +" is "+decodedString

	except IndexError:
		print "The string index is out of range "

	except:
		print "There is a bug in the program"

hashedInt = int(input("Enter the number: "))
print "The hash " +str(hashedInt)
reverse_hash(hashedInt)

# hashedString =	680131659347
# print "The string is " +str(hashedString)

# print letters[0]
# print letters[15]


