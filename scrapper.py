import requests
import json
req = requests.get('https://beta.nseindia.com/api/equity-stockIndices?index=NIFTY%2050').json()
del req['advance']
del req['name']
del req['timestamp']
del req['metadata']
l = list(req.items())
t = l[0][1]
i = 0
symb = input("Enter your Stock Symbol: ")
symb = symb.upper()
while i < len(t):
    t = dict(l[0][1][i])
    if t['symbol'] == symb:
        print(t['symbol'])
        break
        
    i+=1
