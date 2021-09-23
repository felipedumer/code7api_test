import boto3
import os

# Conexão com o dynamodb
dynamodb = boto3.resource('dynamodb')
TABLE = os.getenv('DYNAMODB_TABLE')

def search(values, searchFor):
    found = []
    for k in values:
        for v in k:
            if searchFor.lower() in k[v].lower():
                found.append(k)
    return found

def handler(event, context):
    print(event)

    # Especificando tabela
    table = dynamodb.Table(TABLE)
    
    tableResult = table.scan()

    print(tableResult)

    tableResult = tableResult['Items']

    searchResult = search(tableResult, event['body']['searchBy'])

    print(searchResult)

    response = {
        'statusCode': 200,
        'data': searchResult,
    }
    
    return response