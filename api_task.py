import  requests
url="https://catfact.ninja/fact"
response=requests.get(url)
if(response.status_code==200):
  data=response.json()
  print("-" *20)
  print(data["fact"])
else:
  print("failed to fetch data")
