import sys
from PyDictionary import PyDictionary
dictionary=PyDictionary()
def eng2oth(valu):
    #print valu
    svalu=valu.split()
    for i in range(len(svalu)):
         print str(i)
         print str(svalu[i])
         print dictionary.translate(svalu[i],'hi')
#capturing value from properties
#values=[]
#count = 0
infilename=sys.argv[1]
ifile=open(infilename, 'r')
for line in ifile:
    
    pair=line.split('=')
    key=str(pair[0]);value=str(pair[1])
    
    #print value
    
    #count=count +1
    eng2oth(value)
    
    
    

#translation code
#for val in value:
 #   print dictionary.translate(val,'hi')


