
import json

items = json.loads('[{"id":1, "title":"First title"}, {"id":2, "title":"Second title"}]')

for item in items:
    print(item['title'])
      
a = 4
if a > 5:
    print('test')
else:
    print('no')
if a <= 5:
    print(4)
if a==5:
    print(3)
    
data = {'a': 0,
        'b': 1,
        'c': 2
}