import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName='company',
    KeySchema=[
        {
            'AttributeName': 'com_id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'com_id',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

 
table.meta.client.get_waiter('table_exists').wait(TableName='company')


print("Table status:", table.table_status)

print('table is creating.......')
table.meta.client.get_waiter('table_exists').wait(TableName='company')

print(table.item_count)

