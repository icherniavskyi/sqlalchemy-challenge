# sqlalchemy-challenge

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

### Temperature Stats (Dates Range)
- **URL:** `/api/v1.0/<start>/<end>`
- **Description:** Returns minimum, average, and maximum temperatures for dates between the start and end date specified by user.

## Additional information and examples are provided in the app's home page
