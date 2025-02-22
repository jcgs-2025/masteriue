# import concurrent.futures
# import time
# import requests

# def download_page(url):
#     response = requests.get(url)
#     return f"{url} - {len(response.content)} bytes"

# urls = [
#     "https://www.python.org",
#     "https://www.github.com",
#     "https://www.google.com"
# ]

# start_time = time.time()

# #ThreadPool - Concurrency #IO dependency
# #ProcessPool - Parallelism #CPU dependecy 

# with concurrent.futures.ThreadPoolExecutor() as executor:
    
#     # Create a future to execute
#     futures = [executor.submit(download_page, url) for url in urls]
    
#     # When the future is done.
#     for future in concurrent.futures.as_completed(futures):
#         print(future.result())
        
# end_time = time.time()
# print(f"Download all pages : {end_time - start_time} seconds")

# PARALLEL COMPUTING

from calculator import series
import concurrent.futures
import time

numbers = [500, 600, 700, 800]

start_time = time.time()

with concurrent.futures.ProcessPoolExecutor() as executor:
    futures = [executor.submit(series.factorial, num) for num in numbers]
    
    for future in concurrent.futures.as_completed(futures):
        print(f"The factorial of {numbers[futures.index(future)]} is {future.result()}")
        
end_time = time.time()
print(f"Calculate all factorials in: {end_time - start_time} seconds")