
﻿

# eBay Search Automation Tools

**Note**: Please be aware this was my first Python project. A lot of conventions/best practices have been violated. At some point I'd like to rewrite this. For the time being though, I still think there's a lot of useful code scattered throughout that could be helpful for others. And of course feel free to submit a pull request for any issues/improvements! Thanks :)

This is a collection of search tools that automate reporting and provide useful analytics for eBay searches. These tools were created with an emphasis in reusability and are easily adapted for a variety of use cases.

## **Features**

- Reports item price history and calculates estimated value
- Reports all active items within user defined constraints
- Creates automated SMS alerts for newly listed items within constraints
- Automatically removes previously alerted items to prevent duplicates
- Filters unnecessary key words using NLP and user defined stop words list
- Highly modular and adheres to the UNIX Design Philosophy
- Designed with serverless architecture in mind (AWS Lambda)

## **Getting Started**

Clone all files from the GitHub repository. Edit the config.py file with your eBay Developer key and phone number.

## **Compatibility**

These tools have been developed and tested on Ubuntu 18.04.1. The software has additionally been tested on Windows 7 x64, Windows 10 x64, Mac OS X High Sierra, and Mac OS X Mojave.

## **Built With**

- [FindingService](https://github.com/timotheus/ebaysdk-python) – eBay RESTful API used to gather eBay item data
- [Requests](http://docs.python-requests.org/en/master/) – Retrieves information from GET requests
- [Boto3](https://github.com/boto/boto3) – AWS Python SDK
- [AWS SNS](https://github.com/tartley/colorama) – Text messaging service
- [AWS Comprehend](https://github.com/tartley/colorama) – Provides sentiment analysis
- [SpaCy](https://github.com/explosion/spaCy) – NLP library for stop word removal and tokenization
- [Colorama](https://github.com/tartley/colorama) - Used to change console text color
- [Matplotlib](https://github.com/matplotlib/matplotlib) - Used to plot graphs

## **Upcoming Changes**

- Implementation of trend lines and linear regression price estimates in main.py
- Implementation of more robust scheduling system
- Add an option for email notifications
- Add an option to select &quot;Text&quot;, &quot;Email&quot;, or &quot;None&quot; notifications
- Increased usage of SpaCy NLP throughout

## **Authors**

- **Jack Owens**  - _Initial work_ -

## **License**

This project is licensed under the MIT License.

## **Acknowledgments**

- Ryan Chesler: YouTube tutorial _&quot;Make an eBay Item Alert System Using Python&quot;_
- Beverly Myers: Assistance with Linear Regression
