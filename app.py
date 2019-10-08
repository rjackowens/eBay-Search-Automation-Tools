import json
import requests
from url_maker import auction_urls
from time_left_converter import timeLeft, timeLeftDay, timeLeftHour, timeLeftMinute

print ("\nAuctions Ending Soonest: \n")

for searchquery in auction_urls:
    results = requests.get(searchquery)
    raw = results.json()

    try:
        for item in (raw["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"]):
            
            price = item["sellingStatus"][0]["convertedCurrentPrice"][0]['__value__']
            time_left = item["sellingStatus"][0]["timeLeft"][0]
            title = item["title"][0]
            url = item["viewItemURL"][0]
            bid_count = item["sellingStatus"][0]["bidCount"][0]
            
            remaining = timeLeft(time_left)
            
            print(f"{title} ${price} \n {remaining} \n {bid_count} bids \n {url} \n")

    except KeyError: # No results found
        pass
        
