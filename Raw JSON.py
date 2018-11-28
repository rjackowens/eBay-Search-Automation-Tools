# Displays Raw JSON Data for Active Listings
import json, requests
from config import key

searchTerm = ("curta")
condition = ("3000")
minPrice =("200")
maxPrice =("1200")

print ("\n1 = Active Listings \n2 = Sold Listings")

operation = input("\nSelect Item Status: ")
if operation == "1":
  operation = "findItemsByKeywords"
elif operation == "2":
  operation = "findCompletedItems"
else:
  print ("You did not select a valid operation")

active_url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=" + operation + "\
&SERVICE-VERSION=1.7.0\
&SECURITY-APPNAME=" + key +"&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=" + condition + "\
&itemFilter(1).name=MinPrice\
&itemFilter(1).value=" + minPrice +"&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue=USD\
&itemFilter(2).name=MaxPrice\
&itemFilter(2).value=" + maxPrice +"&itemFilter(2).paramName=Currency\
&itemFilter(2).paramValue=USD\
&itemFilter(3).name=ListingType\
&itemFilter(3).value(0)=AuctionWithBIN\
&itemFilter(3).value(1)=FixedPrice\
&paginationInput.entriesPerPage=10\
&sortOrder=PricePlusShippingLowest\
&keywords=" + searchTerm)

results = requests.get(active_url)
raw = results.json()
print (raw)