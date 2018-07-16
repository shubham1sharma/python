
#import necessary library

from ipwhois import IPWhois
from pprint import pprint
from warnings import filterwarnings
import socket

print("welcome!")
res=input("enter your name!= ")
print("hello",res)
join=input("enter yes(y) to proceed!=")
if join[0]=="y":
    filterwarnings(action="ignore")         
    # remove all your warnings
    res=input("enter your url=")            
    # enter corresponding url
    res=socket.gethostbyname(res)         
    # search ip address of corresponding url
    obj=IPWhois(res)                        
    # pass whois request
    xyz=obj.lookup_whois()                
    # look for corresponding ip address
    pprint(xyz)

elif join[0]=="n":                           
    print("we'r taking you back")
    res=input("press e to exit")
    
    if res[0]=="e":
        exit(0)
    else:
        pass
else:
    print("invalid")



