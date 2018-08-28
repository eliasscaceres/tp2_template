# Imports
from flask import Flask
from flask import render_template
from aux_pro import Process
from database import Database
from flask import redirect

app = Flask(__name__)

db = Database()
pro = Process()

@app.route('/')
def index():
	# pro.start_process()
	return render_template('index.html',is_running=pro.is_running())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

@app.route('/start', methods = ["POST"])
def start():
    
    # If there is a process running, return to index()
    if pro.is_running():
   		pro.stop_process()
    else:
    	pro.start_process()
    return redirect("/")

@app.route('/promedios')
def average():
	tempavg = 0
	windavg = 0
	pressavg = 0
	humavg = 0
	samples = db.get_10_last_samples()
	cant = len(samples)
	if (cant>0):
		for i in samples:
			tempavg += i['temperature']
			windavg += i['windspeed']
			humavg += i['humidity']
			pressavg += i['pressure']
	tempavg=round(tempavg/cant,2)
	windavg=round(windavg/cant,2)
	humavg=round(humavg/cant,2)
	pressavg=round(pressavg/cant,2)
	return render_template('promedios.html',tempavg=tempavg ,humavg=humavg,windavg=windavg,pressavg=pressavg)

@app.route('/envivo')
def vivo():
	sample = db.get_sample()
	lasttemp = sample['temperature']
	lastwind = sample['windspeed']
	lasthum = sample['humidity']
	lastpress = sample['pressure']
	return render_template('envivo.html',temp=lasttemp , hum=lasthum, wind=lastwind, press=lastpress)

@app.route('/ultimo')
def ultimo():
	sample = db.get_sample()
	lasttemp = round(sample['temperature'],2)
	lastwind = round(sample['windspeed'],2)
	lasthum = round(sample['humidity'],2)
	lastpress = round(sample['pressure'],2)
	return render_template('ultimo.html',temp=lasttemp , hum=lasthum, wind=lastwind, press=lastpress)	