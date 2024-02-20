import boto3


db = boto3.resource('dynamodb')
table = db.Table("employee")

response = table.get_item(Key={
    'emp_id':'11'
})

print(table.item_count)
print(response['Item'])