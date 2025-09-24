import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # sort the result alphabetically by keys:
# print(json.dumps(x, indent=4, separators=(", ", " = "), sort_keys=true))

x = '{"name":"abish"}'
y = json.loads(x)
print(y) # Returns Python Dictionary