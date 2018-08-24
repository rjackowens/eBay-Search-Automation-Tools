# Currently Listed Items
import json, requests, config
key = config.key

min_price = input("Enter Minimum Price: ")
max_price = input("Enter Maximum Price: ")
search_term = input("Enter Search Term: ")

url = ("http://svcs.ebay.com/services/search/FindingService/v1\
?OPERATION-NAME=findItemsByKeywords\
&sortOrder=PricePlusShippingLowest\
&buyerPostalCode=63011&SERVICE-VERSION=1.13.0\
&SECURITY-APPNAME=" + key +"&RESPONSE-DATA-FORMAT=JSON\
&REST-PAYLOAD\
&itemFilter(0).name=ListingType\
&itemFilter(0).value=FixedPrice\
&itemFilter(1).name=Condition\
&itemFilter(1).value=Used\
&itemFilter(2).name=MinPrice\
&itemFilter(2).value=" + min_price +"&itemFilter(1).paramName=Currency\
&itemFilter(2).paramValue=USD\
&itemFilter(3).name=MaxPrice\
&itemFilter(3).value=" + max_price +"&itemFilter(2).paramName=Currency\
&itemFilter(3).paramValue=USD\
&keywords=" + search_term)
result = requests.get(url)
raw = result.json()

print(raw)

# for item in (raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
#     title = item["title"][0]
#     condition = item['condition'][0]['conditionDisplayName'][0]
#     price = item['sellingStatus'][0]["convertedCurrentPrice"][0]['__value__']
#     print(title + " " + price + " " + condition)

