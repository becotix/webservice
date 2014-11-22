from bottle import route, run, template

@route("/")
def index(name):
	return template('<b>Becotix Webservice 1.0</b>!')

run(host='0.0.0.0', port=80)


