# Real-Time Weather Data Analysis for Multiple U.S. Cities

This project demonstrates a real-time weather data ingestion and analysis pipeline for multiple major U.S. cities. It leverages the [OpenWeatherMap API](https://openweathermap.org/api) to fetch live weather metrics, stores the data in an Apache Spark DataFrame for scalable processing, and uses Spark SQL to extract actionable insights.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [AWS Setup](#aws-setup)
- [Data Ingestion and Processing](#data-ingestion-and-processing)
- [SQL-Based Analysis](#sql-based-analysis)
- [Results](#results)
- [Short Report](#short-report)
- [Conclusion](#conclusion)

## Overview

This project implements a scalable, real-time weather monitoring system that:
- Continuously fetches weather data for multiple U.S. cities.
- Processes and stores the JSON responses using Apache Spark.
- Executes SQL queries to analyze temperature extremes, average temperature, city-specific weather, humidity trends, and the frequency of weather conditions.

## Features

- **Real-Time Data Ingestion:** Retrieves weather metrics every 30 seconds.
- **Scalable Processing:** Utilizes Apache Spark DataFrames for distributed data storage and processing.
- **SQL-Based Analysis:** Performs complex queries to extract meaningful insights from the weather data.
- **Insightful Reporting:** Summarizes key metrics such as temperature extremes, average temperatures, and humidity levels.

## AWS Setup

The solution is deployed on AWS and involves:
1. Configuring an environment to support real-time data ingestion.
2. Integrating the OpenWeatherMap API for continuous weather data retrieval.
3. Utilizing Apache Spark for distributed processing of the acquired data.

<img width="476" alt="image" src="https://github.com/user-attachments/assets/a69c349e-8c8f-49c0-949d-459b28a97e86" />


## Data Ingestion and Processing

- **Script:** The main Python script `weather_analysis.py` is responsible for fetching, parsing, and storing the weather data.
- **Data Storage:** The structured JSON responses from the API are ingested into an Apache Spark DataFrame.
- **Commands:**
  ```bash
  nano weather_analysis.py
  cat weather_analysis.py

(The above commands show how the file was created and its content displayed.)

<img width="468" alt="image" src="https://github.com/user-attachments/assets/fff9e3d9-6187-421f-946f-cfea7a68452e" />
<img width="468" alt="image" src="https://github.com/user-attachments/assets/ea5956d0-ff4f-41d0-a994-5f85a275c803" />
<img width="468" alt="image" src="https://github.com/user-attachments/assets/f2e8301b-6338-45cd-9cac-50232d61a110" />
<img width="468" alt="image" src="https://github.com/user-attachments/assets/23266d19-912b-4679-b32d-02f3943e783f" />

SQL Analysis:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/66d718eb-4c54-47d9-8bd8-da186dc495cc" />

Results

The SQL-based queries provide detailed insights into the weather data:
	•	Temperature Extremes: A maximum of 24.61°C and a minimum of 2.51°C highlight the broad range of conditions.
	•	Average Temperature: The overall average temperature of approximately 9.56°C offers a baseline of the overall weather across the selected cities.
	•	City Trends: Miami emerges as the warmest city while Denver registers the coldest conditions.
	•	Humidity: Cities such as Dallas, Seattle, Miami, and New York experience periods of high humidity (above 80%).
	•	Weather Distribution: The data shows a predominance of “Clear” conditions, with fewer occurrences of “Mist” and “Rain.”

Short Report

Summary of Data Collected

A real-time data ingestion pipeline was established to continuously fetch weather metrics from the OpenWeatherMap API for major U.S. cities. The data captured includes:
	•	Temperature: Recorded in °C.
	•	Humidity: Measured as a percentage.
	•	Weather Conditions: Such as Clear, Clouds, Rain, etc.
	•	Timestamp: Indicating the exact time of recording.

Data was collected over a two-hour interval with records captured every 30 seconds, resulting in a high-resolution temporal dataset. The JSON responses were parsed and ingested into an Apache Spark DataFrame, enabling efficient and scalable querying.

Observations from SQL Queries
	•	Temperature Extremes:
The analysis identified a maximum temperature of 24.61°C and a minimum of 2.51°C across all cities.
	•	Average Temperature:
The overall average temperature was calculated to be approximately 9.56°C, establishing a baseline for further analysis.
	•	City-Specific Trends:
	•	Warmest City: Miami with a peak temperature of 24.61°C.
	•	Coldest City: Denver with a temperature of 2.51°C.
	•	Humidity Dynamics:
Cities experiencing high humidity (>80%) include Dallas, Seattle, Miami, and New York, indicative of transient weather phenomena.
	•	Weather Condition Frequency:
The distribution shows “Clear” conditions as the most prevalent, followed by “Clouds”, while “Mist” and “Rain” are less frequent.

Insights
	•	Temperature Variability:
Significant fluctuations in temperature reflect both inter-city and intra-city variations, likely driven by microclimatic factors and urban heat island effects.
	•	Humidity Dynamics:
Elevated humidity levels may signal transient weather events such as precipitation or increased dew points.
	•	Weather Conditions:
The predominant occurrence of clear skies provides insight into the overall favorable weather conditions during the data collection period.
	•	Scalability:
Utilizing Apache Spark for data ingestion and processing ensures the system can efficiently handle high-frequency data and large datasets.

Conclusion

This project successfully establishes a real-time weather monitoring system by integrating data ingestion from the OpenWeatherMap API with scalable processing using Apache Spark. The detailed SQL-based analysis offers valuable insights into temperature variations, humidity trends, and the distribution of weather conditions across multiple U.S. cities. This system exemplifies the power of real-time data analytics in understanding and forecasting complex meteorological phenomena.
