import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
import concurrent.futures
from statistics import mean, median, variance, mode

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_temperature(city):
    url = f"https://weather.siel.com.co/city/{city}/temp/max"
    headers = {
        "Content-Type": "application/json-patch+json",
        "Accept": "application/json-patch+json",
        "Authorization": "Bearer secret-token-1234",
    }
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=10)
        response.raise_for_status()
        response_data = response.json()
        return response_data, city
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {str(e)}")
        return [], city

def calculate_statistics(city):
    return {
        "mean": mean(city),
        "median": median(city),
        "variance": variance(city),
        "mode": mode(city)
    }

def concurrent_(cities):
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = {executor.submit(get_temperature, city): city for city in cities}
        
        for future in concurrent.futures.as_completed(futures):
            result, city = future.result()
            
            if not result:
                print(f"Error downloading {city}")
                continue
            
            stats = parallel_(result)
            if stats is not None:
                print(f"The city is: {city}, mean: {stats['mean']}, median: {stats['median']}, variance: {stats['variance']}, mode: {stats['mode']}")
            else:
                print(f"No temperature data available for {city}")
    except Exception as e:
        print(f"Error: {str(e)}")

def parallel_(city):
    if not city:
        return None
    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(calculate_statistics, city)
            return future.result()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

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

    concurrent_(cities)