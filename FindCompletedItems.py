# Jack Owens 8/23/2018 
# Finds Completed eBay Listings
import json, requests, config, colorama
from colorama import init, Fore
init()

searchTerm = input ("\nEnter Search Term: ")
minPrice = input("Enter Minimum Price: ") # Enter %00 to hard code no min price
maxPrice = input("Enter Maximum Price: ") # Enter %00 to hard code no max price
print ("\n1 = New \n2 = Used \n3 = For Parts or Not Working")

condition = input("\nSelect Condition: ")
if condition == "1":
    condition = "1000"
elif condition == "2":
    condition = "3000"
elif condition == "3":
    condition = "7000"
else: 
    print ("You did not select a valid category")
    
# Change Category via itemFilter(0).Value:
# 1000 New | 1500 New Other | 1750 New With Defects |2000 Manufacture Refurbrished | 2500 Seller Refurbrished | 4000 Very Good | 5000 Good | 6000 Acceptable | 7000 Parts or Not Working

# Edit config.py with your eBay Developer Key
key = config.key
url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findCompletedItems\
&SERVICE-VERSION=1.7.0\
&SECURITY-APPNAME=" + key +"&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=3000\
&itemFilter(1).name=FreeShippingOnly\
&itemFilter(1).value=true\
&itemFilter(2).name=SoldItemsOnly\
&itemFilter(2).value=true\
&itemFilter(3).name=MinPrice\
&itemFilter(3).value=" + minPrice +"&itemFilter(1).paramName=Currency\
&itemFilter(3).paramValue=USD\
&itemFilter(4).name=MaxPrice\
&itemFilter(4).value=" + maxPrice +"&itemFilter(2).paramName=Currency\
&itemFilter(4).paramValue=USD\
&sortOrder=PricePlusShippingLowest\
&paginationInput.entriesPerPage=100\
&keywords=" + searchTerm)

result = requests.get(url)
raw = result.json()

print ("\n--------------------------")
print (Fore.YELLOW + "\nMost Recent Sold Listings: \n" + Fore.GREEN)
for item in (raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
    title = item["title"][0]
    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
    print (title + " $" + price)
    #sum(float(price))

