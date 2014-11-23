from bottle import route, get, post, run, template, request
from datetime import *
from db import *
import json  

@route("/")
def index():
	return { "name": "Becotix Webservice 1.0",
			 "supported_methods":"register,stop_info,tickets,journey_data,travelhistory,personaldetails"}

@post("/register")
def register():
	name = request.query['name']
	email = request.query['email']
	address1 = request.query['address_1']
	address2 = request.query['address_2']
	city = request.query['city']
	region = request.query['region']
	postcode = request.query['postcode']
	cc_hash = request.query['cc_hash']
	password = request.query['password_hash']
	cursor.execute("INSERT INTO user VALUES (default,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,email,address1,address2,city,region,postcode,cc_hash,password))
	return { "name": "register", "result":"successful", "uid":cursor.lastrowid}

@get("/stop_info")
def stop_info():
	cursor.execute("SELECT * from stop")
	stops = [ dict(line) for line in [ zip([ column[0] for column in cursor.description ], 
                 row) for row in cursor.fetchall() ] ]
	cursor.execute("SELECT * from beacon")
	beacons = [ dict(line) for line in [ zip([ column[0] for column in cursor.description ], 
                 row) for row in cursor.fetchall() ] ]
	return {"name":"stop_info", 
			"stops":stops, "bus_beacons":beacons}

@get("/tickets")
def tickets():
	cursor.execute("SELECT id,colour,word from tickets")
	tickets =  [ dict(line) for line in [ zip([ column[0] for column in cursor.description ], 
                 row) for row in cursor.fetchall() ] ]
	return {"name":"tickets","tickets":tickets}

@get("/journey_data")
def journeydata():
	uid = request.query['uid']
	startid = request.query['startid']
	stopid = request.query['stopid']
	starttime = request.query['starttime']
	stoptime = request.query['stoptime']
	journeys = "successful"
	cursor.execute("INSERT INTO journey VALUES (default,%s,%s,%s,%s,%s,%s)",(uid,startid,stopid,starttime,stoptime,journeys))
	return {"name":"journeys", 
				"result":journeys}

@get("/travelhistory")
def travelhistory():
	cursor.execute("SELECT * from journey")
	travelhistory = [ dict(line) for line in [ zip([ column[0] for column in cursor.description ], 
                 row) for row in cursor.fetchall() ] ]
	return {"name":"travelhistory",
			"travelhistory":travelhistory}

@get("/personaldetails")
def personaldetails():
	cursor.execute("SELECT * from user")
	userdata = [ dict(line) for line in [ zip([ column[0] for column in cursor.description ], 
                 row) for row in cursor.fetchall() ] ]
	return {"name":"personaldetails",
			"personaldetails":userdata}

run(host='0.0.0.0', port=80)
