# Synchrnous programming

import time 
def fetch_weather():
    print("Fetching weather data")
    time.sleep(2) #simulate the network delay
    print("Weather data fetch")
    
def fetch_news():
    print("Fetching weather data")
    time.sleep(2) #simulate the network delay
    print("Weather data fetch")

def main():
    start_time = time.time()
    
    fetch_weather()
    fetch_news()
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
    
main()

# Asynchrnous programming

import asyncio
import time

async def fetch_weather():
    print("Fetching weather data")
    await asyncio.sleep(2)  # simulate network delay
    print("Weather data fetched")

async def fetch_news():
    print("Fetching news data")
    await asyncio.sleep(2)  # simulate network delay
    print("News data fetched")

async def main():
    start_time = time.time()

    await asyncio.gather(
        fetch_weather(),
        fetch_news()
    )

    end_time = time.time()

    print(f"Total time taken: {end_time - start_time:.2f} seconds")

await main()

#Problem with out pydantic

def add_parent_data(name: str , age: int):
    if type(name) == str and type(age)== int:
        if age >=0:
            print(name , age)
            print(" Data added successfully to the database! ")
        else:
            raise ValueError("Age can not be negative.")
    else:
        raise TypeError("Invalid datatype for name or age")
    
def update_parent_data(name: str , age: int):
    if type(name) == str and type(age)== int:
        if age >=0:
            print(name , age)
            print(" Data added successfully to the database! ")
        else:
            raise ValueError("Age can not be negative.")
    else:
        raise TypeError("Invalid datatype for name or age")
    
add_parent_data("Ayush", 25)
add_parent_data("Ayush", -25)




