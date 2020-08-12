# Import Dependences
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


# Define what to do when a user hits the index route
@app.route("/")
def home():   
    print("Server received request for 'Home' page...")
    
    """List all available api routes."""
    return (
        f"<strong>Available Routes:</strong><br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/datesearch start:/<start><br/>"
        f"<i>Example datesearch: /api/v1.0/datesearch start:/2017-05-01</i><br/>"
        f"/api/v1.0/datesearch/start:/<start> end:/<end><br/>"
        f"<i>Example datasearch: /api/v1.0/datesearch/start:/2017-05-01end:/2018-05-01<i>"
    
    )


# Define what to do when a user hits the /api/v1.0/precipitation route
# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.
@app.route("/api/v1.0/precipitation")
def precipitation():   
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # determine year
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    # query last 12 months of prec data
    year_results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago).all()

    session.close()

    # Create a dictionary from the data and append to a list of measurements_data
    measurements_data = []
    for date, prcp in year_results:
        measurements_dict = {}
        measurements_dict["Date"] = date
        measurements_dict["Precipitation"] = prcp
        measurements_data.append(measurements_dict)

    return jsonify(measurements_data)

    print("Server received request for 'Precipitation' page...")


# Define what to do when a user hits the /api/v1.0/stations route
# /api/v1.0/stations route will return a json list of stations
@app.route("/api/v1.0/stations")
def stations():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query list of stations 
    station_results = session.query(Measurement.station).group_by(Measurement.station).all()
    
    session.close()

    # create dictionary from the data and append to a list of station_data
    station_data = []
    for station in station_results:
        station_dict = {}
        station_dict["Station"] = station
        station_data.append(station_dict)  

    return jsonify(station_data)


    #stations_list = list(np.ravel(station_results))
    #return jsonify(stations_list)

    print("Server received request for 'Stations' page...")

# Define what to do when a user hits the /api/v1.0/tobs route
# /api/v1.0/tobs route will return a json list of temperature observations (TOBS) for the previous year
@app.route("/api/v1.0/tobs")
def tobs():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query list of stations
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365) 
    tobs_results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= year_ago).filter(Measurement.station == 'USC00519397').all()

    session.close()

    #create dictionary from the data and append to a list of tobs_data
    tobs_data = []
    for date, tobs in tobs_results:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Temperature Obs"] = tobs
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)

    print("Server received request for 'tobs' page...")


# Define what to do when a user hits start/end page
#/api/v1.0/<start> and /api/v1.0/<start>/<end> will return a json listing the min, avg, and max temperatures for given start/end dates
@app.route('/api/v1.0/datesearch start:/<start>')
def start_search(start):

    session = Session(engine)
    
    start_search = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs), ).\
        filter(func.strftime("%Y-%m-%d",Measurement.date) >= start).group_by(Measurement.date).all()         

    #create dict from data and append to a list of search_data
    search_data = []
    for a,b,c,d in start_search:
        start_dict = {}
        start_dict["Date"] = a
        start_dict["Min Temp"] = b
        start_dict["Max Temp"] = c
        start_dict["Avg Temp"] = d
        search_data.append(start_dict)

    return jsonify(search_data)
    print("Server received request for 'start_search' page")

@app.route('/api/v1.0/datesearch/start:/<start>end:/<end>')
def start_end_search(start, end):

    session = Session(engine)
    
    start_end_search = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
        filter(func.strftime("%Y-%m-%d",Measurement.date) >= start).\
        filter(func.strftime("%Y-%m-%d",Measurement.date) <= end).\
        group_by(Measurement.date).all() 

    # create dict from data and append to a list of search_data2
    search_data2 = []
    for a,b,c in start_end_search:
        search_dict = {}
        search_dict["Min Temp"] = a
        search_dict["Max Temp"] = b
        search_dict["Avg Temp"] = c
        search_data2.append(search_dict)

    return jsonify(search_data2)
    print("Server received request for 'start_end_search' page")

if __name__ == "__main__":
    app.run(debug=True)