import boto3
import os

# Conexão com o dynamodb
dynamodb = boto3.resource('dynamodb')
TABLE = os.getenv('DYNAMODB_TABLE')

def handler(event, context):
    print(event)

    # Especificando tabela
    table = dynamodb.Table(TABLE)
    
    table.delete_item(
        Key={
            'id': event['body']['id']
        },
    )

    response = {
        'statusCode': 200,
        'message': 'Notícia deletada com sucesso!'
    }
    
    return response