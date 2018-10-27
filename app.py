import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_, or_, not_

from statistics import stdev
from datetime import date, timedelta


from flask import Flask, jsonify

##########################################################
# Database setup
#
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()                        # reflect sqlite database
Base.prepare(engine, reflect=True)           # reflect the tables
Measurement = Base.classes.measurement       # Save references to each table
Station = Base.classes.station

session = Session(engine)                    # Create session from Python to the DB

##########################################################
# Flask Setup
app = Flask(__name__)
###########################################################
#Flask routes

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start_date>"
        f"/api/v1.0/<start_date>/<end_date"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
#######################################################
#return date and precipitation values from one year before last date in data set
# in json form

    # get last date
    last_tuple=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date=last_tuple[0]
    # find "1 year ago"
    date_list=last_date.split('-')
    year=int(date_list[0])
    month=int(date_list[1])
    day=int(date_list[2])
    year_ago= date(year,month,day) - timedelta(days=365)
    year_ago_date_str=str(year_ago)
    year_ago_date_str
    # query previous years data
    data_set=session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year_ago_date_str).order_by(Measurement.date)
    # put into dictionary
    date_index=[record[0] for record in data_set]
    prcp_values=[record[1] for record in data_set]
    prcp_dict=dict(zip(date_index,prcp_values))
    return jsonify(prcp_dict)

@app.route("/api/v1.0/stations")
def stations():
#########################################################
#  Return a JSON list of stations from the dataset.

    # List the stations and the counts in descending order.
    station_entrys=session.query(Station.name,Station.station).distinct().all()
    station_dict={}
    for record in station_entrys:
        station_dict[record[0]]=record[1]
    return jsonify(station_dict)


if __name__ == '__main__':
    app.run(debug=True)

'''
`/api/v1.0/precipitation`

 `/api/v1.0/stations`

  `/api/v1.0/tobs`

  `/api/v1.0/<start>`

  `/api/v1.0/<start>/<end>`'''