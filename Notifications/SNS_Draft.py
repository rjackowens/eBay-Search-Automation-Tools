# Install AWS CLI via "pip install awscli"
# Run "configure"
# Verify, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_DEFAULT_REGION env variables are set

import boto3
from config import number

aws_client = boto3.client("sns")

sns_phone_number = "+1XXXXXXXXXX"
sns_message = "Test."
#sns_subject = "This is the subject of the message"

aws_response = aws_client.publish(
    #TopicArn='TEST TOPIC',
    PhoneNumber=sns_phone_number,
    Message=sns_message,
    #Subject=sns_subject,
)
 
##############################

import boto3

sns_phone_number = "+1XXXXXXXXXXX" #Enter Phone Number in E.164 Format
sns_message = "This is a test SNS message."

client = boto3.client(
    "sns",
    region_name = "us-east-1"
    aws_access_key_id="XXXXXXXXXXXXXX", #For best practice use AWS_ACCESS_KEY_ID env variable
    aws_secret_access_key="XXXXXXXXXXXXXX", #For best practice use AWS_SECRET_ACCESS_KEY env variable
)

response = client.publish(
    PhoneNumber=sns_phone_number,
    Message=sns_message,
)

 # client = boto3.client(
#     'sns',
#     region_name = "us-east-1"
#     aws_access_key_id="XXXXX",
#     aws_secret_access_key="XXXXX",
# )
#     TopicArn='EXAMPLE',
#     PhoneNumber='+1XXXXXXXXXXX',
#     Message='Test Message from SNS',
#     Subject='Test',
#     MessageAttributes={
#         'string': {
#             'DataType': 'string',
#             'StringValue': 'string',
#             'BinaryValue': b'bytes'
#         }
#     }
# )