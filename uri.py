import re
def getScheme(uri):
	try :
		temp= uri.index(":")
		scheme = uri[:temp]
		print "Scheme of the url : " + str(scheme)
		return uri[temp+1:]
	except :
		print "NO scheme or bug in the program"

def getDomain(domainString):
	try :
		temp1=domainString.replace('//','')
		# print temp1.split('.')
		L=temp1.split('/')[0].strip()
		print "Domain name : " + str(L)
		return L
	except :
		print "Error in getting domain"
def changeTLD(domainName):
	schemes=['http','https','ssl','callto','mailto','cvs','feedready']
	tlds= ['com','io','in','co.in','org','xyz','uk']

	for scheme in schemes :
		for tld in tlds:
			if scheme =='callto' or scheme =='mailto':
				print 'uri is [ ' + scheme+':'+domainName+tld+' ]'
			else :
				
				print 'uri is [ ' + scheme+'://'+'www.'+domainName+'.'+tld+' ]'	
# 'http://stackoverflow.com/questions/24594351/python-regexp-to-check-if-string-is-tld-domain'
uri = input("Enter the URI: ")
temp= getScheme(uri)
# temp1=temp.replace('//','')
# # print temp1.split('.')
# print temp1.split('/')
domainName=getDomain(temp)
changeTLD(domainName.split('.')[0].strip()) # when www is not present
changeTLD(domainName.split('.')[1].strip()) # when wwww is present 


