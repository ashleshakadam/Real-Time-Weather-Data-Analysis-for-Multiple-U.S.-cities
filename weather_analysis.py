#!/usr/bin/env python
import requests
import json
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min

# Replace with your actual OpenWeatherMap API key
API_KEY = "758fce6dd3722cf25cd213a13bbc5484"

# List of cities to monitor
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Miami", "Dallas", "Seattle", "Denver", "Boston"
]


def fetch_weather_data():
    records = []
    for city in cities:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            record = {
                "city": city,
                "temperature": float(data.get("main", {}).get("temp", 0.0)),  # Ensure float
                "humidity": int(data.get("main", {}).get("humidity", 0)),     # Ensure int
                "weather": data.get("weather")[0]["main"] if data.get("weather") else None,
                "timestamp": int(data.get("dt", 0))                           # Ensure int
            }
            records.append(record)
        else:
            print(f"Failed to fetch weather data for {city}: {response.status_code}")
    return records

def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("WeatherAnalysis").getOrCreate()
    
    # List to accumulate weather data over time
    weather_data = []
    
    # Calculate end time (2 hours from start)
    end_time = time.time() + 2 * 60 * 60  # 2 hours in seconds
    
    while time.time() < end_time:
        print("Fetching weather data...")
        new_records = fetch_weather_data()
        weather_data.extend(new_records)
        print(f"Fetched {len(new_records)} records. Total records so far: {len(weather_data)}")
        time.sleep(30)  # Wait 30 seconds before the next fetch
    
    # Create a Spark DataFrame from the collected data
    df = spark.createDataFrame(weather_data)
    
    # Register DataFrame as a temporary SQL table
    df.createOrReplaceTempView("weather_data")
    
    # --- SQL Queries ---

    # 1. Identify hottest and coldest recorded temperatures
    query_temp_extremes = """
    SELECT MAX(temperature) as hottest, MIN(temperature) as coldest FROM weather_data
    """
    extremes = spark.sql(query_temp_extremes)
    print("Hottest and Coldest Recorded Temperatures:")
    extremes.show()

    # 2. Find the average temperature in USA based on these cities
    query_avg_temp = """
    SELECT AVG(temperature) as avg_temperature FROM weather_data
    """
    avg_temp = spark.sql(query_avg_temp)
    print("Average Temperature in USA (selected cities):")
    avg_temp.show()

    # 3. Find the warmest and coldest cities (based on the latest records)
    query_warmest_city = """
    SELECT city, temperature FROM weather_data
    ORDER BY temperature DESC LIMIT 1
    """
    warmest = spark.sql(query_warmest_city)
    print("Warmest City:")
    warmest.show()

    query_coldest_city = """
    SELECT city, temperature FROM weather_data
    ORDER BY temperature ASC LIMIT 1
    """
    coldest = spark.sql(query_coldest_city)
    print("Coldest City:")
    coldest.show()

    # 4. Identify cities with high humidity (>80%)
    query_high_humidity = """
    SELECT DISTINCT city FROM weather_data WHERE humidity > 80
    """
    high_humidity = spark.sql(query_high_humidity)
    print("Cities with High Humidity (>80%):")
    high_humidity.show()

    # 5. Count of weather conditions recorded
    query_weather_counts = """
    SELECT weather, COUNT(*) as condition_count FROM weather_data GROUP BY weather
    """
    weather_counts = spark.sql(query_weather_counts)
    print("Count of Weather Conditions:")
    weather_counts.show()
    
    # Stop the Spark session when done
    spark.stop()

if __name__ == "__main__":
    main()
