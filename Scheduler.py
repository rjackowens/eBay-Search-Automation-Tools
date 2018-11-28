import json
import requests
import boto3
from config import key, number
from CalculateAverage import calculate_average
from colorama import init, Fore
init()

# Prompts User to Enter Search Term, Min/Max Price, and Condition
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

# API Request for Sold Listings
url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findCompletedItems\
&SERVICE-VERSION=1.7.0\
&SECURITY-APPNAME=" + key +"&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=" + condition + "\
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
&paginationInput.entriesPerPage=25\
&keywords=" + searchTerm)

sold_results = requests.get(url)
sold_raw = sold_results.json()

# API Request for Active Listings
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
&itemFilter(3).value(0)=AuctionWithBIN\
&itemFilter(3).value(1)=FixedPrice\
&paginationInput.entriesPerPage=25\
&sortOrder=PricePlusShippingLowest\
&keywords=" + searchTerm)

active_results = requests.get(active_url)
active_raw = active_results.json()

# Calculates Average Sold Price
new_list1=[]
for item in (sold_raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
  price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  title = item["title"][0]
  int_price = int(float(price))
  new_list1.append(int_price)

average_sold_price = (calculate_average(new_list1))

# Calculates Average Active Price
new_list2=[]
new_list3 = []
for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
  price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  title = item["title"][0]
  int_price = int(float(price))
  new_list2.append(int_price)
  new_list3.append(title)

average_active_price = (calculate_average(new_list2))

#print (new_list1) # List of All Sold Prices
#print (new_list2) # List of All Active Prices
#print (new_list3) # Displays Active Items

dictionary = dict(zip(new_list3, new_list2))

for key, value in dictionary.items():
  if value < average_sold_price:
    dict_string = (key, "$" + str(value))
    print (dict_string)
#     client = boto3.client('sns')
#     response = client.publish(
#         PhoneNumber= number
#         Message=(str(key) + str(value)),
#         Subject='Test Subject',
# )




# This assigns all price values with a value lower than average sold price to discounted_items_price
discounted_items_price = []

for item in new_list2:
    if item < average_sold_price:
        discounted_items_price.append(item)
        #print (item)  

#print (discounted_items_price)

# Average Sold Price: 893.25

# This assigns all item strings with a value lower than average sold price to discounted_items_item
#discounted_items_item = []

# Displays Active Items Listed Below Average Sold Price
# print (Fore.YELLOW + "\nActive Listings Below Sold Price: \n" + Fore.GREEN)
# for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
#    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
#    title = item["title"][0]
#    url = item["viewItemURL"][0]
#    if float(price) < average_sold_price: # Filters Out Expensive Items
#        print (title + " $" + price + " \nLink: " + url + "\n")