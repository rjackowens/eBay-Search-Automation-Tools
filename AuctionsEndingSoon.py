import json
import requests
from config import key, number
from time_left_converter import timeLeft, timeLeftDay, timeLeftHour, timeLeftMinute

searchTerm = "Jaeger LeCoultre -vintage -clock -atmos" 
condition = ("3000") #Pre-owned
minPrice =("600")
maxPrice =("7000")
minBids = "1"

active_url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
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
&itemFilter(3).value(0)=Auction\
&itemFilter(4).name=MinBids\
&itemFilter(4).value=" + minBids + "\
&paginationInput.entriesPerPage=100\
&sortOrder=EndTimeSoonest\
&keywords=" + searchTerm)

results = requests.get(active_url)
raw = results.json()

#print(raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"])

new_list = []

print ("\nListings Ending Soonest: \n")
for item in (raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
   price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
   time_left = item["sellingStatus"][0]["timeLeft"][0]
   title = item["title"][0]
   url = item["viewItemURL"][0]
   bid_count = item["sellingStatus"][0]["bidCount"][0]

   remaining = timeLeft(time_left)

   print (title + " $" + price + "\n" + remaining + " \n" + bid_count + " bids \n" + url + "\n")
   int_price = int(float(price))
   new_list.append(int_price)

