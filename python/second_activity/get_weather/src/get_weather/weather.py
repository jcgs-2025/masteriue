import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
import concurrent.futures

def get_temperature (city):

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
    
    
def concurrent_(city):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(get_temperature, city)
    
    for future in concurrent.futures.as_completed([future]):
        result, city = future.result()
        print(f"The result is: {result}")
        print(f"The result of city is: {city}")

city = [
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

for i in city:
    result = concurrent_(i)
    print(f"The result is:", result)


    
    
    

# def parallel_get_temperature(city_list):
#     if city_list == None or len(city_list) == 0:
#        return None
   
#     try:
#         e =2 
#         with concurrent.futures.ThreadPoolExecutor() as executor:
#             results = executor.map(get_temperature,cities)    
#     except Exception as e:
#         print(f"Error to procesing the paralellism {city}: {str(e)}")
#         return None   
    