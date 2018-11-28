# Displays average item active price and sends as text message
import json
import requests
import boto3
from config import key, number
from colorama import init, Fore
init()

def calculate_average(x):
   return sum(x) / float(len(x))

searchTerm = input ("\nEnter Search Term: ")
condition = ("3000")
minPrice =("200")
maxPrice =("1200")

# minPrice = input("Enter Minimum Price: ") # Enter %00 to hard code no min price
# maxPrice = input("Enter Maximum Price: ") # Enter %00 to hard code no max price
# print ("\n1 = New \n2 = Used \n3 = For Parts or Not Working")

# condition = input("\nSelect Condition: ")
# if condition == "1":
#   condition = "1000"
# elif condition == "2":
#   condition = "3000"
# elif condition == "3":
#   condition = "7000"
# else:
#   print ("You did not select a valid category")

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

results = requests.get(active_url)
raw = results.json()

new_list = []

print (Fore.YELLOW + "\nActive Listings: \n" + Fore.GREEN)
for item in (raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
   price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
   title = item["title"][0]
   url = item["viewItemURL"][0]
   print (title + " $" + price + " \nLink: " + url + "\n")
   int_price = int(float(price))
   new_list.append(int_price)

print (Fore.YELLOW + "Average Active Price: \n" + Fore.GREEN)
average_active_price = (calculate_average(new_list))
print (average_active_price)

# Send Text Message via AWS SNS 
aws_client = boto3.client("sns")
sns_phone_number = number

sns_message = "The average price of " + searchTerm + " is $" + str(average_active_price)

aws_response = aws_client.publish(
    PhoneNumber=sns_phone_number,
    Message=sns_message,
)
