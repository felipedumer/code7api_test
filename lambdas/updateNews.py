import boto3
from datetime import datetime
import os

# Conexão com o dynamodb
dynamodb = boto3.resource('dynamodb')
TABLE = os.getenv('DYNAMODB_TABLE')

def handler(event, context):
    print(event)

    # Especificando tabela
    table = dynamodb.Table(TABLE)
    
    result = table.update_item(
        Key={
            'id': event['body']['id']
        },
        ExpressionAttributeNames={
        '#newsTitle' : 'title',
        '#newsText' : 'text',
        '#updatedAt' : 'updated_at',
        },
        ExpressionAttributeValues={
          ':title': event['body']['title'],
          ':newsText': event['body']['text'],
          ':updatedAt': (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"),
        },
        UpdateExpression='SET #newsTitle = :title, #newsText = :newsText, #updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    response = {
        'statusCode': 200,
        'data': result['Attributes'],
        'message': 'Notícia atualizada com sucesso!'
    }
    
    return response