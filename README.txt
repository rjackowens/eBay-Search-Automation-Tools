eBay Price History Tool:
This tool utilizes the eBay FindingService API operation "findCompletedItems" to query completed eBay listings and calculate
average sold prices. The program returns aggregate pricing data and allows the user to create a notification of
items listed within a defined price constraint. 

Upcoming Changes:
An upcoming version of the program will use regression analysis to analyze historical data to predict future price trends. 

Prerequisites:
This tool requires an installation of Python3.

Getting Started:
Download all files included within GitHub repository. Edit the config.py file with your eBay developer key.  

Built With:
eBay FindingService API - Used to gather item data 
Requests - Used to parse HTTP requests
Colorama - Used to add color to console text
boto3 - AWS SDK used for SNS notifications
matplotlib - Used to plot graphs

Authors:
Jack Owens - Initial work -

License:
This project is licensed under the MIT License.

Acknowledgments:
Ryan Chesler for his excellent YouTube tutorial "Make an Ebay Item Alert system using Python 3.6" 
