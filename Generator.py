import json

x = {"test":{"a":1,"b":2}, "test2":2}

with open("data.json",'w') as f:
    json.dump(x,f)

with open('data.json','r') as f:
    y=json.load(f)

print(y["test"])