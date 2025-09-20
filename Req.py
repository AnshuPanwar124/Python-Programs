import requests

r = requests.get("https://www.geeksforgeeks.org/javascript/web-api-url/")
print(r.text)
print(r.status_code)

#url = "www.something.com"
#data = {

 #   "p1":4,
  #  "p2":8
#}

#r2 = requests.post(url=url, data=data)

payload = {'username': 'test', 'password': 'test123'}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)


