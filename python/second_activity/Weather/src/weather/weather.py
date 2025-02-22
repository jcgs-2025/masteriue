from calculator import series
import concurrent.futures
import time


token = "secret-token-1234"

url = "https://weather.siel.com.co/city/"

headers = {
    "Authorization": f"Bearer {token}"
}

cities = ["London", "New York", "Paris", "Tokyo", "Sydney", "Moscow", "Cairo", "Rio", "Mumbai", "Beijing"]

curl -H "Authorization: Bearer secret-token-1234" https://weather.siel.com.co/city/paris/temp/max
 

for city in cities:
    response = requests.get(f"{url}{city}/temp/max", headers=headers)
    print(f"{city} - {response.json()}")