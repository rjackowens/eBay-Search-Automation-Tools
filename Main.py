import json
import requests
import boto3
from config import key, number 
from CalculateAverage import calculate_average
from colorama import init, Fore
init()

# # Function to Calculate Average
# def calculate_average(x):
#    return sum(x) / float(len(x))

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
&itemFilter(3).value=" + minPrice +"&itemFilter(1).paramName=Currency\
&itemFilter(3).paramValue=USD\
&itemFilter(4).name=MaxPrice\
&itemFilter(4).value=" + maxPrice +"&itemFilter(2).paramName=Currency\
&itemFilter(4).paramValue=USD\
&sortOrder=PricePlusShippingLowest\
&paginationInput.entriesPerPage=100\
&keywords=" + searchTerm)

sold_results = requests.get(sold_url)
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
&paginationInput.entriesPerPage=10\
&sortOrder=PricePlusShippingLowest\
&keywords=" + searchTerm)

active_results = requests.get(active_url)
active_raw = active_results.json()

# Displays Average Sold Price
new_list1=[]

print (Fore.YELLOW + "\nAverage Sold Price: \n" + Fore.GREEN)
for item in (sold_raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
  price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  title = item["title"][0]
  int_price = int(float(price))
  new_list1.append(int_price)

average_sold_price = (sum(new_list1) / float(len(new_list1)))
print (average_sold_price)
print ("") # New Line

# Displays Average Active Price
new_list2=[]

print (Fore.YELLOW + "Average Active Price: \n" + Fore.GREEN)
for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
  price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  title = item["title"][0]
  int_price = int(float(price))
  new_list2.append(int_price)

average_active_price = (calculate_average(new_list2))
print (average_active_price)

# Displays Recent Sold Listings
print (Fore.YELLOW + "\nRecent Sold Listings: \n" + Fore.GREEN)
for item in (sold_raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
  title = item["title"][0]
  price2 = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  print (title + " $" + price2)

# Displays Current Active Listings
print (Fore.YELLOW + "\nActive Listings: \n" + Fore.GREEN)
for item in (active_raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
   price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
   title = item["title"][0]
   url = item["viewItemURL"][0]
   print (title + " $" + price + " \nLink: " + url + "\n")
   int_price = int(float(price))
   new_list1.append(int_price)

# Send Average Item Price Text Messages via AWS SNS 
aws_client = boto3.client("sns")
sns_phone_number = number

active_message = "The average active price of " + searchTerm + " is $" + str(average_active_price)

aws_response = aws_client.publish(
    PhoneNumber=sns_phone_number,
    Message=(active_message)
)

sold_message = "The average sold price of " + searchTerm + " is $" + str(average_sold_price)

aws_response = aws_client.publish(
    PhoneNumber=sns_phone_number,
    Message=(sold_message)
)