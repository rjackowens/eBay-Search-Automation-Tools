import boto3
import json
from config import number

comprehend = boto3.client(service_name="comprehend", region_name="us-east-1")
           
item_description = "Selling a used JLC master ultra thin. I got it as a gift and don't use it. It is caliber 839." # Example Item Description 

# Calling DetectSentiment
sentiment_results = (comprehend.detect_sentiment(Text=item_description, LanguageCode="en")["Sentiment"])

print("Sentiment = " + sentiment_results)

if sentiment_results == "NEGATIVE":
    print("Result = FAIL")
    # Fail Conditions...
else:
    print("Result = PASS")
    # Pass Conditions...
