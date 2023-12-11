# Import Python dependencies
import numpy as np
import pandas as pd
import datetime as dt

# Import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Flask Setup
from flask import Flask, jsonify

# Database setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
print(Base.classes.keys())
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Set up Flask

app = Flask(__name__)


# Flask Routes
@app.route("/")
def index():
    return(
    '''
    Welcome to my Climate Analysis API!<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/<start>/<end><br/>
    ''')
    
# Create routes

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in data set.   
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Perform a query to retrieve the data and precipitation scores from previous year
    precipitation = session.query(Measurement.date,Measurement.prcp).\
        filter(Measurement.date >= query_date).all()
        
    # Create a dictionary to hold a key/value pair
    prcp_dict = {date: prcp for date, prcp in precipitation}
    return jsonify(prcp_dict)

# Station Route

@app.route("/api/v1.0/stations")
def stations():
    # Count total number of stations
    results = session.query(Station.station).all()
    
    # Unravel results into 1-dimensional array using 'function np.ravel()', 'parameter = results'
    
    # Convert array into a list
    stations = list(np.ravel(results))
    return jsonify (stations=stations)

# Most Active Station Temperature Route

@app.route("/api/v1.0/tobs")
def station_temp():
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= query_date).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)


# Statistics for Start and End Date Route
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def statistics(start=None, end=None):
    
    # Find min, max, avg temps. Put in list called select.
    select = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    # Determine start/end dates
    if end != None:
        
        results = session.query(*select).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        print(temps)
        return jsonify(temps=temps)
    else:
        results = session.query(*select).\
        filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        print(temps)
        return jsonify(temps=temps)
    
if __name__ == "__main__":
    app.run()