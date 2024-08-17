import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Posts')

def lambda_handler(event, context):
    post_id = event['PostID']
    post_text = event['Text']
    hashtags = event['Hashtags']
    
    # Prepare item to insert into DynamoDB
    item = {
        'PostID': post_id,
        'Text': post_text,
        'Hashtags': json.dumps(hashtags),  # Convert the list of hashtags to a string to store in DynamoDB
        'Timestamp': str(datetime.utcnow())
    }
    
    # Put the item into the DynamoDB table
    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'body': json.dumps('Post added successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error adding post: {str(e)}')
        }
