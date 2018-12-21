import json
import requests
import boto3
from config import key, number
from colorama import init, Fore
init()

# Prompts User to Enter Search Term, Min/Max Price, and Condition
search_term = input ("\nEnter Search Term: ")
min_price = input("Enter Minimum Price: ") # Enter %00 to hard code no min price
max_price = input("Enter Maximum Price: ") # Enter %00 to hard code no max price

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
sold_url = ("http://svcs.ebay.com/services/search/FindingService/v1\
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
&itemFilter(3).value=" + min_price +"&itemFilter(1).paramName=Currency\
&itemFilter(3).paramValue=USD\
&itemFilter(4).name=MaxPrice\
&itemFilter(4).value=" + max_price +"&itemFilter(2).paramName=Currency\
&itemFilter(4).paramValue=USD\
&sortOrder=PricePlusShippingLowest\
&paginationInput.entriesPerPage=100\
&keywords=" + search_term)

sold_results = requests.get(sold_url)
# sold_raw = sold_results.json()

try:
  sold_raw = sold_results.json()
except ValueError: #json.decoder.JSONDecodeError
  print (Fore.RED + "\nNo Listings Found. JSONDecodeError has Occured." + Fore.RESET)
  #pass # Throws exception at line 75

# API Request for Active Listings
active_url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&SERVICE-VERSION=1.7.0\
&SECURITY-APPNAME=" + key +"&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=Condition\
&itemFilter(0).value=" + condition + "\
&itemFilter(1).name=MinPrice\
&itemFilter(1).value=" + min_price +"&itemFilter(1).paramName=Currency\
&itemFilter(1).paramValue=USD\
&itemFilter(2).name=MaxPrice\
&itemFilter(2).value=" + max_price +"&itemFilter(2).paramName=Currency\
&itemFilter(2).paramValue=USD\
&itemFilter(3).name=ListingType\
&itemFilter(3).value(0)=AuctionWithBIN\
&itemFilter(3).value(1)=FixedPrice\
&paginationInput.entriesPerPage=100\
&sortOrder=PricePlusShippingLowest\
&keywords=" + search_term)

active_results = requests.get(active_url)
# active_raw = active_results.json()

try:
  active_raw = active_results.json()
except ValueError: #json.decoder.JSONDecodeError
  print (Fore.RED + "\nNo Listings Found. JSONDecodeError has Occured." + Fore.RESET)

# Displays Average Sold Price
new_list1=[]
print (Fore.YELLOW + "\nAverage Sold Price: \n" + Fore.GREEN)

try:
  for item in (sold_raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
    title = item["title"][0]
    int_price = int(float(price))
    new_list1.append(int_price)
except KeyError:
  print (Fore.RED + "\nNo Listings Found. KeyError Has Occured." + Fore.RESET)

try:
  def calculate_average(x):
    return sum(x) / float(len(x))
  average_sold_price = (calculate_average(new_list1))
  print (average_sold_price)
  print ("") # New Line
except ZeroDivisionError:
  print (Fore.RED + "\nNo Listings Found. ZeroDivisionError Has Occured." + Fore.RESET)

# Displays Average Active Price
new_list2=[]
print (Fore.YELLOW + "Average Active Price: \n" + Fore.GREEN)

try:
  for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
    title = item["title"][0]
    int_price = int(float(price))
    new_list2.append(int_price)
except KeyError:
  print (Fore.RED + "\nNo Listings Found. KeyError Has Occured." + Fore.RESET)

try:
  average_active_price = (calculate_average(new_list2))
  print (average_active_price)
except ZeroDivisionError:
  print (Fore.RED + "\nNo Listings Found. ZeroDivisionError Has Occured." + Fore.RESET)

###################################

# Displays Recent Sold Listings
print (Fore.YELLOW + "\nRecent Sold Listings: \n" + Fore.GREEN)

try:
  for item in (sold_raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
    title = item["title"][0]
    url = item["viewItemURL"][0]
    price2 = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
    print (title + ":" + Fore.YELLOW + " $"  + price2 + " " + Fore.BLUE + url + Fore.GREEN)
except KeyError:
  print (Fore.RED + "\nNo Listings Found. KeyError Has Occured." + Fore.RESET)

# Displays Current Active Listings
print (Fore.YELLOW + "\nActive Listings: \n" + Fore.GREEN)

try:
  for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
    price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
    title = item["title"][0]
    url = item["viewItemURL"][0]
    print (title + ":" + Fore.YELLOW + " $"  + price + " " + Fore.BLUE + url + Fore.GREEN)
except KeyError:
  print (Fore.RED + "\nNo Listings Found. KeyError Has Occured." + Fore.RESET)

# Imports Previously Alerted Items
with open("itemid.txt", "r") as item_file:
   itemids = item_file.read().splitlines()

# Init AWS SNS
aws_client = boto3.client("sns")
sns_phone_number = number

# Text Message Alerting + Item Filtering
print (Fore.YELLOW + "\nListings to Alert: \n" + Fore.GREEN)

for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
 item_id = item["itemId"][0]
 price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
 title = item["title"][0]
 url = item["viewItemURL"][0]
 int_price = int(float(price))
 
 if int_price < average_sold_price and item_id not in itemids: # Removes previously alerted items and items over the average sold price
   print(title + ":" + Fore.YELLOW + " $"  + price + " " + Fore.BLUE + url + Fore.GREEN)   
  
   # Send AWS Text Alert
   sns_message = (title + ":" + " $"  + price + " " + url)
   aws_response = aws_client.publish(
     PhoneNumber=sns_phone_number,
     Message=sns_message,
  )

  # Adds Items to Previously Alerted Items 
   with open("itemid.txt", "a") as item_file:
     item_file.write((item_id + "\n"))
 else:
  continue
