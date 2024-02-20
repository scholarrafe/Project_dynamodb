import boto3

db = boto3.resource('dynamodb')
table = db.Table('company')


{'emp_id' : '3','name' : 'nafi','age': '29'}

table.put_item(
    Item={'com_id' : '1','name' : 'ancova','ceo': 'Rayhan'}
)


print("execution")