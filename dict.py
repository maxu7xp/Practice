import json

x = '{"name":"john", "age": "24"}'

y = json.loads(x)

print(y["name"])