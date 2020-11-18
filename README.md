SQLAlchemy Project

The purpose of this project was to do some climate analysis for Honolulu, Hawaii to determine whether  specified timeframe would meet my criteria for an enjoyable holiday vacation.

### Part 1: Climate Analysis and Exploration

To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database (hawaii.sqlite) for a time period of my choosing. The analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib. 

* SQLAlchemy (`create_engine`) was used to connect to the sqlite database.

* Used SQLAlchemy `automap_base()` to reflect tables into classes and saved a reference to those classes called `Station` and `Measurement`.

### Part 2: Precipitation Analysis

* Designed a query to retrieve the last 12 months of precipitation data.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

* Used Pandas to print the summary statistics for the precipitation data.

### Part 3: Station Analysis

* Designed a query to calculate the total number of stations.

* Designed a query to find the most active stations.

  * Listed the stations and observation counts in descending order.

  * Listed which station has the highest number of observations;

* Designed a query to retrieve the last 12 months of temperature observation data (TOBS).

  * Filtered by the station with the highest number of observations.

  * Plotted the results as a histogram with `bins=12`.

- - -

## Part 5: Climate App

Now that I completed my initial analysis, I designed a Flask API based on the queries that I just developed.

* Used Flask to create the routes.

### Routes

* `/`

  * Home page.

  * Lists all routes that are available.

* `/api/v1.0/precipitation`

  * Converts the query results to a dictionary using `date` as the key and `prcp` as the value.

  * Returns the JSON representation of your dictionary.

* `/api/v1.0/stations`

  * Returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Queries the dates and temperature observations of the most active station for the last year of data.
  
  * Returns a JSON list of temperature observations (TOBS) for the previous year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculates `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculates the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

- - -

## Bonus: Other Analyses

### Temperature Analysis I

* Identified the average temperature in June at all stations across all available years in the dataset. Did the same for December temperature for comparative purposes.

* Used the t-test to determine whether the difference in the means, if any, is statistically significant. 

### Temperature Analysis II

* Utilized a function called `calc_temps` that will accept a start date and end date in the format `%Y-%m-%d`. The function will return the minimum, average, and maximum temperatures for that range of dates.

* Used the `calc_temps` function to calculate the min, avg, and max temperatures for your trip using the matching dates from the previous year.

* Plotted the min, avg, and max temperature from previous query as a bar chart.

  * Used the average temperature as the bar height.

  * Used the peak-to-peak (TMAX-TMIN) value as the y error bar (YERR).


### Daily Rainfall Average

* Calculated the rainfall per weather station using the previous year's matching dates.

* Calculated the daily normals. Normals are the averages for the min, avg, and max temperatures.

* Utilized a function called `daily_normals` that will calculate the daily normals for a specific date. 

* Create da list of dates for my trip in the format `%m-%d`. Used the `daily_normals` function to calculate the normals for each date string and appended the results to a list.

* Loaded the list of daily normals into a Pandas DataFrame and set the index equal to the date.

* Used Pandas to plot an area plot (`stacked=False`) for the daily normals.


Thank you for visiting my GitHub.

Arlette Varela