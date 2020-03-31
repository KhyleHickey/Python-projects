# -*- coding: utf-8 -*-
"""
Python: 3.8
@author: Khyle
"""

import urllib.request       #test for internet
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
    
print( 'connected' if connect() else 'no internet' )



from urllib.request import Request, urlopen   #checks to see if website is online
from urllib.error import URLError, HTTPError
req = Request("http://stackoverflow.com")
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    print ('Website is working fine')

    
    
def connect(trgthost='www.quora.com'):     #attempts to connect to website 
    try:
        urllib.request.urlopen(trgthost) 
        return True
    except:
        return False
# test
print( 'Test successful' if connect() else 'no internet')

    
