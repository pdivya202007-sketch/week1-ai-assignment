import requests # importing requests library
city="hyderabad"   #declaring city
url=f"https://wttr.in/{city}?format=3"    # this is middle one (url)
data=requests.get(url)   # SERVER requests
print(data.text)