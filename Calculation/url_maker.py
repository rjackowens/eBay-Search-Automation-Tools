from config import *

with open("search_terms.txt") as f:
    items = f.read().splitlines()

auction_urls = []

for item in items:

    URL = ("http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.7.0&SECURITY-APPNAME=" + key +"&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&itemFilter(0).name=Condition&itemFilter(0).value=" + condition + "&itemFilter(1).name=MinPrice&itemFilter(1).value=" + minPrice + "&itemFilter(1).paramName=Currency&itemFilter(1).paramValue=USD&itemFilter(2).name=MaxPrice&itemFilter(2).value=" + maxPrice + "&itemFilter(2).paramName=Currency&itemFilter(2).paramValue=USD&itemFilter(3).name=ListingType&itemFilter(3).value(0)=Auction&itemFilter(4).name=MinBids&itemFilter(4).value=" + minBids + "&paginationInput.entriesPerPage=100&sortOrder=EndTimeSoonest&keywords=" + item)
    auction_urls.append(URL)
