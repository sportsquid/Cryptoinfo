import sys
import json

#url stuff
import urllib3 
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')

#function to get data from url
def getJSON ( url ):
  data = json.loads(http.request('GET', url).data.decode(encoding='UTF-8',errors='ignore'))
  return data

  

#error if no commands
if len(sys.argv) <= 1:
  print("Error: please supply argumnets or type 'help' for help\n")
  exit()

#help command
if len(sys.argv) > 1 and sys.argv[1] == "help":
  print("type in two cryptocurrencies to see the price of the first relative to the second")
  exit()

#list command error
if len(sys.argv) <= 2 and sys.argv[1] == "list":
  print("Improper usage of List. please provide a search term")
  exit()
#list command
if len(sys.argv) > 2 and sys.argv[1] == "list":
  url = "https://min-api.cryptocompare.com/data/all/coinlist"
  data = json.loads(http.request('GET', url).data.decode(encoding='UTF-8',errors='ignore'))
  for coin in data["Data"]:
    if data["Data"][coin]["FullName"].lower().find(sys.argv[2].lower()) != -1:
      print(data["Data"][coin]["FullName"])
  exit()
  
if len(sys.argv) == 2:
  coin1 = sys.argv[1].upper()
  coin2 = "USD"
  source = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(coin1, coin2)
  data = getJSON(source)
  try:
    print("One {} is worth {} {}".format(coin1, data[coin2], coin2))
  except:
    print(data["Message"])
  exit()

if len(sys.argv) == 3:
  coin1 = sys.argv[1].upper()
  coin2 = sys.argv[2].upper()
  source = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}".format(coin1, coin2)
  data = getJSON(source)
  try:   
    print("One {} is worth {} {}".format(coin1, data[coin2] , coin2))
  except:
     print(data["Message"])
  exit()
