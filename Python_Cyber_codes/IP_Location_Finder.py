import requests

ip_address = input("Enter an IP address: ")
data = requests.get("https://ipinfo.io/"+ip_address+"/json").json()
city = data.get("city")
country = data.get("country")
loc = data.get("loc")
region = data.get("region")
print(f"City: {city}\nCountry: {country}\nRegion: {region}\nLocation: {loc}\n")