import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Posts')

def lambda_handler(event, context):
    post_id = event['PostID']
    text = event['Text']
    hashtags = event['Hashtags']
    timestamp = datetime.utcnow().isoformat()
   
    table.put_item(
        Item={
            'PostID': post_id,
            'Text': text,
            'Hashtags': hashtags,
            'Timestamp': timestamp
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Post saved successfully!')
    }
