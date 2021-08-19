#AUTHOR: ANISH KUMAR
#EMAIL: anish5256@gmail.com
import requests
import json
req = requests.get('https://beta.nseindia.com/api/equity-stockIndices?index=NIFTY%2050').json()
del req['advance']
del req['name']
del req['timestamp']
del req['metadata']
l = list(req.items())
t = l[0][1]
iterator = 0
symb = input("Enter your Stock Symbol: ")
symb = symb.upper()
while iterator <= len(t):
    t = dict(l[0][1][i])
    if t['symbol'] == symb:
        print("LTP:",t['lastPrice'])
        print("change: %.2f" % t['change'])
        print("%CHANGE: ",t['pChange'],"%")
        print("OPEN:",t['open'])
        print("DAY LOW:",t['dayLow'])
        print("DAY HIGH:",t['dayHigh'])
        print("CLOSE:",t['previousClose'])
        break
    if iterator==len(t) and t['symbol'] != symb:
        print("PLESE ENTER VALID SYMBOL")
    iterator+=1
    
