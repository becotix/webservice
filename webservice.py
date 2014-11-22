from bottle import route, get, post, run, template

@route("/")
def index():
	return { "name": "Becotix Webservice 1.0"}

@post("/register")
def register():
	return { "name": "register" }
def register(name,email,address1,address2,city,region,postcode,cc_hash,password_hash):
	return { "name": "register", "result":"successful"}

@get("/stop_info")
def stop_info():
	stop = {"stop":{"name":"bus_stop1","major":"9000", "minor":"9000"}}
	beacon = {"bus_beacon":{"minor":"9000","major":"9000"}}
	return {"name":"stop_info", 
			"stops":[stop,stop,stop,stop], "bus_beacons":[beacon,beacon,beacon,beacon]}

run(host='0.0.0.0', port=80)


