import boto3
from datetime import datetime
import uuid
import os

# Conexão com o dynamodb
dynamodb = boto3.resource('dynamodb')
TABLE = os.getenv('DYNAMODB_TABLE')

def handler(event, context):
    print(event)

    # Especificando tabela
    table = dynamodb.Table(TABLE)

    generatedId = str(uuid.uuid4())
    title = event['body']['title']
    text = event['body']['text']
    author = event['body']['author']
    created_at = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    # Salvando dados
    result = table.put_item(
        Item={
            'id': generatedId,
            'title': title,
            'text': text,
            'author': author,
            'created_at': created_at,
            'updated_at': created_at
        }
    )

    print(result)

    response = {
        'statusCode': 200,
        'id': generatedId,
        'message': 'Notícia cadastrada com sucesso!'
    }
    
    return response