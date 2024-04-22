import json
import boto3
from decimal import Decimal

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('dhruv-crc-database')
tableName = 'dhruv-crc-database'

def lambda_handler(event, context):
    
    data = json.loads(event['body'])
                
    table.put_item(Item=data)

    return {
        'statusCode': 200,
        'body': json.dumps({"message" : "Data stored in db"})
    }
