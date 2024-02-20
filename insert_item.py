import boto3


db = boto3.resource('dynamodb')

table = db.Table('employee')


items_to_put=[
    {'emp_id' : '1','name' : 'shofiq','age': '29'},
    {'emp_id' : '2','name' : 'saikot','age': '27'},
    {'emp_id' : '3','name' : 'nafi','age': '29'},
    {'emp_id' : '4','name' : 'Rafe','age': '26'},
    {'emp_id' : '5','name' : 'kashem','age': '27'},
    {'emp_id' : '6','name' : 'masud','age': '29'},
    {'emp_id' : '7','name' : 'nirab','age': '26'},
    {'emp_id' : '8','name' : 'pavel','age': '29'},
    {'emp_id' : '9','name' : 'rahat','age': '27'},
    {'emp_id' : '10','name' : 'rakib','age': '29'},
    {'emp_id' : '11','name' : 'khayrul','age': '27'},
    {'emp_id' : '12','name' : 'shanto','age': '24'},
    {'emp_id' : '13','name' : 'sakib','age': '29'},
    {'emp_id' : '14','name' : 'siam','age': '28'},
    ]

for item in items_to_put:
    table.put_item(
        Item=item
    )

print('yes I am executed')