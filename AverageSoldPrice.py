# Displays average item sold price and sends as text message
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

result = requests.get(sold_url)
raw = result.json()

new_list=[]

print (Fore.YELLOW + "\nRecent Sold Listings: \n" + Fore.GREEN)
for item in (raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
  title = item["title"][0]
  price2 = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  print (title + " $" + price2)
print ("") # New Line

print (Fore.YELLOW + "\nAverage Sold Price: \n" + Fore.GREEN)
for item in (raw["findCompletedItemsResponse"][0]["searchResult"][0]["item"]):
  price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
  title = item["title"][0]
  int_price = int(float(price))
  new_list.append(int_price)

average_sold_price = (calculate_average(new_list))
print (average_sold_price)

# Send Text Message via AWS SNS 
aws_client = boto3.client("sns")
sns_phone_number = number

sns_message = "The average price of " + searchTerm + " is $" + str(average_sold_price)

aws_response = aws_client.publish(
    PhoneNumber=sns_phone_number,
    Message=sns_message,
)
