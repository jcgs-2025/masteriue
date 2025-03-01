import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
import concurrent.futures

def get_temperature(city):
  url = f"https://weather.siel.com.co/city/{city}/temp/max"
  headers = {
    'Content-Type': 'application/json-patch+json',
    'Accept': 'application/json-patch+json',
    'Authorization': 'Bearer secret-token-1234',
  }
  try:
      response = requests.get(url, headers=headers, verify=False, timeout=10)
      response.raise_for_status()
      response_data = response.json()
      return response_data, city
  except requests.exceptions.RequestException as e:
      return e

if __name__ == "__main__":
    cities = [
        "London",
        "New York",
        "Paris",
        "Tokyo",
        "Sydney",
        "Moscow",
        "Cairo",
        "Rio",
        "Mumbai",
        "Beijing",
    ]

    for city in cities:
        result = get_temperature(city)
        print(result)
        
# Run the code and check the output

