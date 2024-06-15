# Citation for the following function:
# Date: 05/22/2024
# Copied from /OR/ Adapted from /OR/ Based on
# the format of this code is based on the source below,
# but is hand authored by the Trek Tracer team.
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Database connection configuration
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = ""
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = ""
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

app.config["DEBUG"] = True


mysql = MySQL(app)
# Route for the home page
@app.route("/")
def home():
    return redirect("/index")

# Route for eventRegistrations page, SELECT data from eventRegistrations table
@app.route("/eventRegistrations", methods=["POST", "GET"])
def eventRegistrations():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        query = "SELECT registrationID, eventID, hikerID, registrationTime FROM EventRegistrations"
        cur.execute(query)
        data = cur.fetchall()
        # Select eventID, eventName from events table
        event_query = "SELECT eventID, eventName FROM Events"
        cur.execute(event_query)
        event_data = cur.fetchall()
        # Select hikerID, userName from hiker table
        hiker_query = "SELECT hikerID, userName FROM Hikers"
        cur.execute(hiker_query)
        hiker_data = cur.fetchall()
        return render_template("eventRegistrations.html", data=data, event_data=event_data, hiker_data=hiker_data)

# Route to INSERT a row into the database for the eventRegistrations page
@app.route("/addEventRegistration", methods=["POST"])
def addEventRegistration():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        eventID = request.form["addEventID"]
        hikerID = request.form["addHikerID"]
        registrationTime = request.form["addRegistrationTime"]
        query = "INSERT INTO EventRegistrations (eventID, hikerID, registrationTime) VALUES (%s, %s, %s)"
        cur.execute(query, (eventID, hikerID, registrationTime))
        mysql.connection.commit()
        return redirect("/eventRegistrations")

# Route to UPDATE a row in the database for the eventRegistrations page
@app.route("/editEventRegistration", methods=["POST"])
def editEventRegistration():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        registrationID = request.form["editRegistrationID"]
        eventID = request.form["editEventID"]
        hikerID = request.form["editHikerID"]
        registrationTime = request.form["editRegistrationTime"]
        query = "UPDATE EventRegistrations SET eventID = %s, hikerID = %s, registrationTime = %s WHERE registrationID =%s"
        cur.execute(query, (eventID, hikerID, registrationTime, registrationID))
        mysql.connection.commit()
        return redirect("/eventRegistrations")

# Route to delete row from eventRegistrations table
@app.route("/deleteEventRegistration", methods=["POST"])
def deleteEventRegistration():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        registrationID = request.form["deleteRegistrationID"]
        query = "DELETE FROM EventRegistrations WHERE registrationID = %s"
        cur.execute(query, (registrationID,))
        mysql.connection.commit()
        return redirect("/eventRegistrations")


# Route for events page, SELECT data from events table
@app.route("/events", methods=["POST", "GET"])
def events():
        cur = mysql.connection.cursor()
        if request.method == "GET":
            query = "SELECT eventID, eventName, eventDate, weather, eventInfo FROM Events"
            cur.execute(query)
            data = cur.fetchall()
            return render_template("events.html", data=data)

# Route to INSERT a row into the database for the events page
@app.route("/addEvent", methods=["POST"])
def addEvent():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        eventName = request.form["eventName"]
        eventDate = request.form["eventDate"]
        weather = request.form["weather"]
        eventInfo = request.form["eventInfo"]
        query = "INSERT INTO Events (eventName, eventDate, weather, eventInfo) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (eventName, eventDate, weather, eventInfo))
        mysql.connection.commit()
        return redirect("/events")

# Route to UPDATE a row in the database for the events page
@app.route("/editEvent", methods=["POST"])
def editEvent():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        eventID = request.form["editEventID"]
        eventName = request.form["editEventName"]
        eventDate = request.form["editEventDate"]
        weather = request.form["editWeather"]
        eventInfo = request.form["editEventInfo"]
        query = "UPDATE Events SET eventName = %s, eventDate = %s, weather = %s, eventInfo = %s WHERE eventID = %s"
        cur.execute(query, (eventName, eventDate, weather, eventInfo, eventID))
        mysql.connection.commit()
        return redirect("/events")

# Route to delete row from events table
@app.route("/deleteEvent", methods=["POST"])
def deleteEvent():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        eventID = request.form["deleteEventID"]
        query = "DELETE FROM Events WHERE eventID = %s"
        cur.execute(query, (eventID,))
        mysql.connection.commit()
        return redirect("/events")


# Route for hikers page, SELECT data from hikers table
@app.route("/index", methods=["POST", "GET"])
def hikers():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        query = "SELECT hikerID, email, userName, biography FROM Hikers"
        cur.execute(query)
        data = cur.fetchall()
        return render_template("index.html", data=data)

# Route to INSERT a row into the database for the hikers page
@app.route('/addHiker', methods=["POST"])
def addHiker():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        email = request.form["email"]
        userName = request.form["userName"]
        biography = request.form["biography"]
        query = "INSERT INTO Hikers (email, userName, biography) VALUES (%s, %s, %s)"
        cur.execute(query, (email, userName, biography))
        mysql.connection.commit()
        return redirect("/index")

# Route to UPDATE a row in the database for the hikers page
@app.route("/editHiker", methods=["POST"])
def editHiker():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        hikerID = request.form["editHikerID"]
        email = request.form["editEmail"]
        userName = request.form["editUsername"]
        biography = request.form["editBiography"]
        query = "UPDATE Hikers SET email = %s, userName = %s, biography =%s WHERE hikerID =%s"
        cur.execute(query, (email, userName, biography, hikerID))
        mysql.connection.commit()
        return redirect("/index")

# Route to delete row from hikers table
@app.route("/deleteHiker", methods=["POST"])
def deleteHiker():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        hikerID = request.form["deleteHikerID"]
        query = "DELETE FROM Hikers WHERE hikerID = %s"
        cur.execute(query, (hikerID,))
        mysql.connection.commit()
        return redirect("/index")


# Route for trails page, SELECT data from trails table
@app.route("/trails", methods=["POST", "GET"])
def trails():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        query = "SELECT trailID, trailName, length, difficulty, trailInfo FROM Trails"
        cur.execute(query)
        data = cur.fetchall()
        return render_template("trails.html", data=data)

# Route to INSERT a row into the database for the trails page
@app.route("/addTrail", methods=["POST"])
def addTrail():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        trailName = request.form["trailName"]
        length = request.form["length"]
        difficulty = request.form["difficulty"]
        trailInfo = request.form["trailInfo"]
        query = "INSERT INTO Trails (trailName, length, difficulty, trailInfo) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (trailName, length, difficulty, trailInfo))
        mysql.connection.commit()
        return redirect("/trails")

# Route to UPDATE a row in the database for the trails page
@app.route("/editTrail", methods=["POST"])
def editTrail():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        trailID = request.form["editTrailID"]
        trailName = request.form["editTrailName"]
        length = request.form["editLength"]
        difficulty = request.form["editDifficulty"]
        trailInfo = request.form["editTrailInfo"]
        query = "UPDATE Trails SET trailName = %s, length = %s, difficulty = %s, trailInfo = %s WHERE trailID = %s"
        cur.execute(query, (trailName, length, difficulty, trailInfo, trailID))
        mysql.connection.commit()
        return redirect("/trails")

# Route to delete row from trails table
@app.route("/deleteTrail", methods=["POST"])
def deleteTrail():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        trailID = request.form["deleteTrailID"]
        query = "DELETE FROM Trails WHERE trailID = %s"
        cur.execute(query, (trailID,))
        mysql.connection.commit()
        return redirect("/trails")


# Route for hikerLogs page, SELECT data from hikerLogs table
@app.route("/hikerLogs", methods=["POST", "GET"])
def hikerLogs():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        query = "SELECT logID, hikerID, trailID, eventID, logTime, difficulty FROM HikerLogs"
        cur.execute(query)
        data = cur.fetchall()
        # Select hikerID, userName from hiker table
        hiker_query = "SELECT hikerID, userName FROM Hikers"
        cur.execute(hiker_query)
        hiker_data = cur.fetchall()
        # Select eventID, eventName from events table
        event_query = "SELECT eventID, eventName FROM Events"
        cur.execute(event_query)
        event_data = cur.fetchall()
        # Select trailID, trailName from trails table
        trail_query = "SELECT trailID, trailName FROM Trails"
        cur.execute(trail_query)
        trail_data = cur.fetchall()
        return render_template("hikerLogs.html", data=data, hiker_data=hiker_data, event_data=event_data, trail_data=trail_data)

# Route to INSERT a row into the database for the hikerLogs page
@app.route("/addHikerLog", methods=["POST"])
def addHikerLog():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        hikerID = request.form["hikerID"]
        trailID = request.form["trailID"]
        eventID = request.form["eventID"]
        logTime = request.form["logTime"]
        difficulty = request.form["difficulty"]
        # Allow null values for foreign keys for hikerID, trailID, eventID
        hikerID = None if hikerID == "" else hikerID
        trailID = None if trailID == "" else trailID
        eventID = None if eventID == "" else eventID
        query = "INSERT INTO HikerLogs (hikerID, trailID, eventID, logTime, difficulty) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (hikerID, trailID, eventID, logTime, difficulty))
        mysql.connection.commit()
        return redirect("/hikerLogs")

# Route to UPDATE a row in the database for the hikerLogs page
@app.route("/editHikerLog", methods=["POST"])
def editHikerLog():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        logID = request.form["editLogID"]
        hikerID = request.form["editHikerID"]
        trailID = request.form["editTrailID"]
        eventID = request.form["editEventID"]
        logTime = request.form["editLogTime"]
        difficulty = request.form["editDifficulty"]
        # Allow null values for foreign keys for hikerID, trailID, eventID
        hikerID = None if hikerID == "" else hikerID
        trailID = None if trailID == "" else trailID
        eventID = None if eventID == "" else eventID
        query = "UPDATE HikerLogs SET hikerID = %s, trailID = %s, eventID =%s, logTime = %s, difficulty = %s WHERE logID = %s"
        cur.execute(query, (hikerID, trailID, eventID, logTime, difficulty, logID))
        mysql.connection.commit()
        return redirect("/hikerLogs")

# Route to delete row from hikerLogs table
@app.route("/deleteHikerLog", methods=["POST"])
def deleteHikerLog():
    cur = mysql.connection.cursor()
    if request.method == "POST":
        logID = request.form["deleteLogID"]
        query = "DELETE FROM HikerLogs WHERE logID =%s"
        cur.execute(query, (logID,))
        mysql.connection.commit()
        return redirect("/hikerLogs")

if __name__ == "__main__":
    app.run(port=9111, debug=True)
