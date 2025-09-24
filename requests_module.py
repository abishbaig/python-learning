import requests
import json

url = 'https://jsonplaceholder.typicode.com/posts/1'
# response = requests.get(url)

# # print(response.status_code)
# serverResponse = response.json()

# print(serverResponse)

# data = {'userId':1,'title': 'foo', 'body': 'bar'}
# response = requests.post(url,json=data)
# print(response.status_code)
# print(response.json())


# data = {'id': 1, 'title': 'foo', 'body': 'bar', 'userId': 1}
# response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
# print(response.status_code)
# print(response.json())


# data = {'title': 'updated title'}
# response = requests.patch('https://jsonplaceholder.typicode.com/posts/1', json=data)
# print(response.status_code)
# print(response.json())

# response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
# print(response.status_code)  # Typically 200 or 204 if successful

# response = requests.head('https://jsonplaceholder.typicode.com/posts/1')
# print(response.status_code)
# print(response.headers)

response = requests.options('https://jsonplaceholder.typicode.com/posts/1')
print(response.status_code)
print(response.headers.get('allow'))  # Shows allowed HTTP methods