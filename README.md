# Real-Time-Weather-Data-Analysis-for-Multiple-U.S.-cities

In this project, I have created a Python script that fetches real-time weather data for
multiple cities in the U.S., stores the data in a structured format using Apache Spark, and
performs SQL-based analysis to extract meaningful insights.

Task Overview:
AWS Setup:
 
1.	Fetch real-time weather data for multiple U.S. cities using OpenWeatherMap API.
2.	Store the fetched data in an Apache Spark DataFrame.
Solution:
•	Implemented a real-time data ingestion pipeline using the OpenWeatherMap API to fetch weather metrics for multiple U.S. cities.
•	Persisted the structured JSON responses into an Apache Spark DataFrame for scalable, distributed processing.

•	The attached screenshots provide technical evidence validating the successful data retrieval and storage operations 
Created weather_analysis.py script using Nano editor.
nano weather_analysis.py

The command cat weather_analysis.py outputs the complete content of the file weather_analysis.py to the terminal. 

cat weather_analysis.py

3.	Perform SQL-based analysis on temperature, humidity, and weather conditions.
Hottest and Coldest Recorded Temperatures:
+-------+-------+                                                               
|hottest|coldest|
+-------+-------+
|  24.61|   2.51|
+-------+-------+

Average Temperature in USA (selected cities):
+-----------------+
|  avg_temperature|
+-----------------+
|9.560161016949147|
+-----------------+

Warmest City:
+-----+-----------+
| city|temperature|
+-----+-----------+
|Miami|      24.61|
+-----+-----------+

Coldest City:
+------+-----------+
|  city|temperature|
+------+-----------+
|Denver|       2.51|
+------+-----------+

Cities with High Humidity (>80%):
+--------+
|    city|
+--------+
|  Dallas|
| Seattle|
|   Miami|
|New York|
+--------+

Count of Weather Conditions:
+-------+---------------+
|weather|condition_count|
+-------+---------------+
|  Clear|           1248|
|   Mist|             25|
| Clouds|            822|
|   Rain|            265|
+-------+---------------+
 

4.	Interpret results and submit findings in a short report.

Short Report: Real-Time Weather Data Collection and Analysis
i.	Summary of Data Collected
A real-time data ingestion pipeline was implemented to continuously fetch weather metrics from the OpenWeatherMap API for multiple major U.S. cities. The data collected includes parameters such as temperature (in °C), humidity (in %), weather conditions (e.g., Clear, Clouds, Rain), and timestamp of recording. The collection process spanned a two-hour interval with data points recorded every 30 seconds, resulting in a high-resolution temporal dataset. The acquired JSON responses were parsed and ingested into an Apache Spark DataFrame, thereby enabling distributed processing and efficient querying through Spark SQL.
ii.	 Observations from SQL Queries
Using Spark SQL, several queries were executed to derive meaningful insights from the accumulated dataset:
•	Temperature Extremes: The SQL queries successfully identified the maximum and minimum recorded temperatures across all cities. The data highlighted considerable variability in temperature readings, reflecting the diverse climatic conditions across the U.S. The extreme values provided a clear indication of the weather dynamics during the data collection window.

The query determined that the maximum recorded temperature was 24.61°C and the minimum was 2.51°C. These extremes underscore the broad range of thermal conditions present across the dataset, likely reflecting the diversity in local climate profiles.

•	Average Temperature: The calculated average temperature across all records provided an aggregated measure of the prevailing weather conditions. This metric was instrumental in establishing a baseline for further comparative analysis among the cities.

The calculated average temperature across the dataset was approximately 9.56°C. This aggregate measure provides a comprehensive baseline reflecting the overall thermal environment among the selected urban areas.

•	City-Specific Analysis: Dedicated queries were used to pinpoint the warmest and coldest cities based on the latest records. The results underscored the heterogeneity in local climates and enabled targeted analysis of urban weather patterns.

The analysis identified Miami as the warmest city, recording a peak temperature of 24.61°C. This result aligns with known regional climatic trends, where coastal and southern locales tend to exhibit higher temperatures.

Conversely, Denver was found to be the coldest, with a recorded temperature of 2.51°C. This finding highlights the impact of elevation and geographic location on the local climate, with Denver’s higher altitude contributing to its lower temperature readings.

•	Humidity Levels: An additional query filtered out records where the humidity exceeded 80%. While duplicates appeared due to varying humidity readings over time, grouping strategies (e.g., using MAX(humidity)) were considered to provide a consolidated view of the highest humidity levels per city. This approach allowed for a more nuanced understanding of atmospheric moisture variations.

The query filtered cities experiencing humidity levels above 80%, revealing that Dallas, Seattle, Miami, and New York had intermittent periods of elevated humidity. This high-humidity condition could be indicative of localized weather events such as rainfall or increased dew points.

•	Weather Condition Frequency: The grouping of weather conditions and their respective counts elucidated the frequency distribution of different weather phenomena. This analysis confirmed the predominance of certain weather types during the data collection period and provided insight into the temporal persistence of various conditions.

The frequency distribution of weather conditions recorded in the dataset was analyzed, yielding the following counts:
•	Clear: 1248 occurrences
•	Mist: 25 occurrences
•	Clouds: 822 occurrences
•	Rain: 265 occurrences
These counts illustrate that “Clear” conditions were predominant, while “Mist” and “Rain” were less frequently observed, potentially corresponding to transient or localized weather phenomena.

iii.	Insights on Temperature, Humidity, and Weather Conditions
The analytical outcomes yielded several key insights:
•	Temperature Variability: The recorded temperature data exhibited significant fluctuations both across different cities and within individual cities over time. This variability suggests that microclimatic factors and urban heat island effects might be influencing the localized temperature patterns. The identification of the warmest and coldest cities supports this assertion, highlighting the differential thermal profiles across the dataset.
•	Humidity Dynamics: The occurrence of high humidity readings (>80%) in multiple cities is indicative of transient weather phenomena such as increased moisture content due to precipitation events or elevated dew points. The data, when aggregated over time, can assist in discerning the correlation between humidity spikes and specific weather conditions, thereby facilitating improved forecasting and climate modeling.
•	Prevalence of Weather Conditions: The frequency analysis of weather conditions revealed a diversified distribution, with certain states exhibiting more dominant patterns (e.g., clear skies versus cloud cover). This distribution is reflective of both seasonal variations and localized meteorological influences. Moreover, the periodic data capture enabled the detection of short-term anomalies or transitions between weather states, thereby enriching the overall understanding of atmospheric behavior.
•	Data Reliability and Scalability: The utilization of Apache Spark for data storage and query execution demonstrated the robustness of the system in handling high-frequency, real-time data ingestion. The scalability of Spark ensured that even as the dataset grew to thousands of records, analytical queries remained performant and yielded actionable insights in a timely manner.
Conclusion
The project successfully established a real-time weather monitoring system that integrates data ingestion from the OpenWeatherMap API with scalable processing via Apache Spark. The rigorous analysis through Spark SQL provided valuable insights into the temperature variations, humidity trends, and prevalent weather conditions across multiple U.S. cities. These findings underscore the importance of real-time data analytics in understanding and forecasting complex meteorological phenomena. The technical evidence, as corroborated by the attached screenshots, validates both the methodology and the efficacy of the implemented system.
