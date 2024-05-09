# sqlalchemy-challenge

# Hawaii Weather Analysis

## This script performs climate analysis for Honolulu, Hawaii based on historical data. Analysis includes examining precipitation and temperature trends over 12 month period. Additionally, station analysis is conducted to identify the most-active stations and investigate temperature observations across various stations. 

## Dependencies
- Python 3.8+
- SQLAlchemy
- pandas
- matplotlib
- numpy
- datetime

### Setup and Usage

1. Open script: hawaii_weather_analysis.py
2. Ensure that the SQLite database hawaii.sqlite is located in the Resources directory
3. Install the required dependencies by running:
``` pip install sqlalchemy pandas matplotlib numpy ```
4. Run the script

## Results and Features

- Uses the SQLAlchemy create_engine() function to connect to the hawaii.sqlite database
- Pulls the last 12 months of precipitation data
- Analyzes precipitation data by sorting values by date, plotting the results, and calculating summary statistics
- Identifies the most-active weather stations 
- Calculates the lowest, highest, and average temperatures observed at the most-active station
- Visualizes the last 12 months of temperature observation

# Climate Analysis API

## This API provides access to climate data stored in a SQLite database that could be found in resources folder. User can retrieve precipitation data, station information, temperature observations, and minimum, maximum, and average temperature for specific date or date ranges.

## Dependencies:
1. Flask:
   - from flask import Flask, jsonify
3. SQLAlchemy:
   - from sqlalchemy import create_engine, func
   - from sqlalchemy.ext.automap import automap_base
   - from sqlalchemy.orm import Session
5. pandas:
   - import pandas as pd
7. datetime:
   - import datetime as dt

## Setup and Installation:

1. After cloning the repository, open app.py file in SurfsUp folder;
2. Install all the dependencies;
3. In the engine object paste the path to your database (hawaii.sqlite file in Resources folder). Example: create_engine("sqlite:///your_path_here");
5. Run the flask application.

## API Routes

### Home Page
- **URL:** `/`
- **Description:** Displays the home page with links to all available API routes.

### Precipitation
- **URL:** `/api/v1.0/precipitation`
- **Description:** Returns the last year's precipitation data as JSON.

### Stations
- **URL:** `/api/v1.0/stations`
- **Description:** Lists all weather observation stations as JSON.

### Temperature Observations
- **URL:** `/api/v1.0/tobs`
- **Description:** Returns the last year's temperature observations from the most active station as JSON.

### Temperature Stats (Start Date)
- **URL:** `/api/v1.0/<start>`
- **Description:** Returns minimum, average, and maximum temperatures for date specified by user. If the date isn't available displays error message.
***Example:***
  - Input: /api/v1.0/2010-01-01
  - Output:
```json
{
"TAVG": 73.09916594176943,
"TMAX": 87.0,
"TMIN": 53.0
}
```

### Temperature Stats (Dates Range)
- **URL:** `/api/v1.0/<start>/<end>`
- **Description:** Returns minimum, average, and maximum temperatures for dates between the start and end date specified by user.
***Example:***
  - Input: /api/v1.0/2010-08-01/2011-05-01
  - Output:
```json
{
  "TAVG": 72.2168284789644,
  "TMAX": 87.0,
  "TMIN": 56.0
}
```

## Additional information and examples are provided in the app's home page
