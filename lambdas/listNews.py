import boto3
import os

# Conexão com o dynamodb
dynamodb = boto3.resource('dynamodb')
TABLE = os.getenv('DYNAMODB_TABLE')

def handler(event, context):
    print(event)

    # Especificando tabela
    table = dynamodb.Table(TABLE)
    
    result = table.scan()

    print(result)

    response = {
        'statusCode': 200,
        'body': result['Items']
    }
    
    return response