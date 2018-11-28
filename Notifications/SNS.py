import boto3
from config import number

def text_message():
    client = boto3.client('sns')
    response = client.publish(
    #TopicArn='TEST TOPIC',
        PhoneNumber='+1XXXXXXXXXX',
        Message='Test message body',
        Subject='Test Subject',
)
