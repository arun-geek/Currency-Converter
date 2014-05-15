import urllib
f=raw_input("Enter Source Currency : ")
t=raw_input("Enter Currency to be converted :")
val=input("Enter Value : ")
url="http://rate-exchange.appspot.com/currency?from="+f+"&to="+t
url=urllib.urlopen(url)
result=url.read()
url.close()
result = result.split()
rate=float(result[3][:7])
print str(val)+" "+f+" is "+str(val*rate)+" "+t
