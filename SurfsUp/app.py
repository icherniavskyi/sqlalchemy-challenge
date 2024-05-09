# Import the dependencies.
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import pandas as pd
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///C:/Users/ulyan/UTOR-VIRT-DATA-PT-02-2024-U-LOLC/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement  = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB

#I decided to create session inside each route due to optimization benefits

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Creating a welcome page with all routes
@app.route("/")
def welcome():
    return ("""
    <h1>SQLAlchemy Challenge</h1>
    <p>Welcome to the my API! Available Routes:</p>
    <p>API Static Routes:</p>
    <ul>
        <li><a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a></li>
        <li><a href="/api/v1.0/stations">/api/v1.0/stations</a></li>
        <li><a href="/api/v1.0/tobs">/api/v1.0/tobs</a></li>
     </ul>
    
    <p>API Dynamic Routes:</p>
        <li>/api/v1.0/start_date</li>
        <li>/api/v1.0/start_date/end_date</li>  
        <p>Replace <strong>start_date</strong> and <strong>end_date</strong> with dates in YYYY-MM-DD format. Exaples:</p>
        <li><a href="/api/v1.0/2010-01-01">/api/v1.0/2010-01-01</a></li>
        <li><a href="/api/v1.0/2010-08-01/2011-05-01">/api/v1.0/2010-08-01/2011-05-01</a></li>
    """)

# Creating a precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Openning new session
    session = Session(bind=engine)
    # Copping the query from the analysis
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date_str = recent_date[0]
    recent_date_norm = dt.datetime.strptime(recent_date_str, '%Y-%m-%d')
    one_year_date = recent_date_norm - dt.timedelta(days=366)
    year_scores = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= one_year_date).\
        order_by(Measurement.date).all()
    
    # Closing session
    session.close()

    # Transforming to dictionary and returning JSON representation
    precipitation = {date: prcp for date, prcp in year_scores}
    return jsonify(precipitation)

# Creating a stations route
@app.route("/api/v1.0/stations")
def stations():
    # Openning new session
    session = Session(bind=engine)
    # Getting stations from station table
    stations_names = session.query(Station.station).all()
    # Closing session
    session.close()

    # Transforming to list and returning JSON representation
    stations = [station[0] for station in stations_names]
    return jsonify(stations)

# Creating tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    # Openning new session
    session = Session(bind=engine)
    # Finding most active station
    active_stations = session.query(Measurement.station, func.count(Measurement.id)).\
                              group_by(Measurement.station).\
                              order_by(func.count(Measurement.id).desc()).all()
    most_act_id = active_stations[0][0]
    
    # Establishing one year period
    recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    recent_date_str = recent_date[0]
    recent_date_norm = dt.datetime.strptime(recent_date_str, '%Y-%m-%d')
    one_year_date = recent_date_norm - dt.timedelta(days=366)
    
    # Collecting data from the most active station for 1 year period
    temp_observ_12 = session.query(Measurement.date, Measurement.tobs).\
    filter(Measurement.station == most_act_id).\
    filter(Measurement.date >= one_year_date).\
        order_by(Measurement.date).all()
    
    # Closing session
    session.close()
    
    # Transforming to dict and returning JSON representation
    temps = {date: temp for date, temp in temp_observ_12}
    return jsonify(temps)

# Dinamic Routes
# Creating routes with start and end varaibles with function get_temps that will query
# the database and parse results according to user's input

@app.route("/api/v1.0/<start>")
def start(start):
    return get_temps(start)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    return get_temps(start, end)

# Deffining get_teps function with end_date as optional argument
def get_temps(start_date, end_date=None):
    session = Session(bind=engine)
    
    # Converting user's input to as string
    start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    if end_date:
        end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    # Prepare the query for temperature statistics
    if end_date:
         results = session.query(func.min(Measurement.tobs), 
                                func.avg(Measurement.tobs),
                                func.max(Measurement.tobs)).\
                    filter(Measurement.date >= start_date).\
                    filter(Measurement.date <= end_date).all()
    else:
        results = session.query(func.min(Measurement.tobs),
                                func.avg(Measurement.tobs),
                                func.max(Measurement.tobs)).\
                      filter(Measurement.date >= start_date).all()

    # Formatting qurering results to a dictionary with corresponding keys
    if results and results[0][0] is not None:
        temps = {
            "TMIN": results[0][0],
            "TAVG": results[0][1],
            "TMAX": results[0][2]
        }
    # If no data in selected dates, returns the message
    else:
        return jsonify({"message": "No data available for this date range. Please select another date."}), 404
    
    return jsonify(temps)


if __name__ == '__main__':
    app.run(debug=True)
    