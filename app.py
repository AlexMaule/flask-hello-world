import sqlalchemy
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
from flask_cors import CORS

from flask import Flask, jsonify

app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to the Project 3 Home Page!<br/>"
        f"<br/>"
        f"Please use the following routes:<br/>"
        f"<br/>"
        f"/api/v1.0/region/(Region)<br>"
        f"   * Choose one of the 4 Regions and replace '(Region)'<br/>"
        f"          - South<br/>"
        f"          - West<br/>"
        f"          - Mid West<br/>"
        f"          - North East<br/>"
        f"<br/>"
        f"/api/v1.0/time/(Region)/(Time)<br>"
        f"   * Choose one of the 4 Regions and replace '(Region)'<br/>"
        f"          - South<br/>"
        f"          - West<br/>"
        f"          - Mid West<br/>"
        f"          - North East<br/>"
        f"   * Choose one of the 4 Time of day and replace '(Time)'<br/>"
        f"          - Early Morning<br/>"
        f"          - Morning<br/>"
        f"          - Afternoon<br/>"
        f"          - Night<br/>"
        f"<br/>"
        f"/api/v1.0/make/(Region)<br>"
        f"     * Choose a Region and replace '(Region)'<br/>"
        f"<br/>"
        f"/api/v1.0/severity/(Region)/(Variable)<br/>"
        f"   * Choose one of the 4 Regions and replace '(Region)'<br/>"
        f"          - South<br/>"
        f"          - West<br/>"
        f"          - Mid West<br/>"
        f"          - North East<br/>"
        f"   * Choose one of the two to replace '(Variable)'<br/>"
        f" - passenger_inj<br/>"
        f" - veh_damage<br/>"
        f"<br/>"
    )

if __name__ == '__main__':
    app.run(debug=True)
