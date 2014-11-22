from bottle import route, get, post, run, template, request
from datetime import *
from db import *

@route("/")
def index():
	return { "name": "Becotix Webservice 1.0"}

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
	stop = {"stop":{"name":"bus_stop1","major":"9000", "minor":"9000"}}
	beacon = {"bus_beacon":{"minor":"9000","major":"9000"}}
	return {"name":"stop_info", 
			"stops":[stop,stop,stop,stop], "bus_beacons":[beacon,beacon,beacon,beacon]}

@get("/tickets")
def tickets():
	ticket = {"word":"cat", "date":datetime.datetime, "color":"#000"}
	return {"name":"tickets",
		"tickets":[ticket,ticket,ticket,ticket]}

@get("/journeydata")
def journeydata():
	return {"name":"journeydata"}

@get("/travelhistory")
def travelhistory():
	return {"name":"travelhistory"}

@get("/personaldetails")
def personaldetails():
	return {"name":"personaldetails"}

run(host='0.0.0.0', port=80)


