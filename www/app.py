# Import de librerias
from flask import Flask
from flask import render_template
from aux_pro import Process
from database import Database
from flask import redirect
from flask import jsonify
from flask import request
import datetime
import os
  
app = Flask(__name__)

db = Database()
pro = Process()

# Ruta inicial
@app.route('/')

# Metodo inicial
def index():
	# pro.start_process()
	return render_template('index.html',is_running=pro.is_running())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

# Metodo para iniciar o detener el muestreo de las variables
@app.route('/start', methods = ["POST"])
def start():
    
    # If there is a process running, return to index()
    if pro.is_running():
   		pro.stop_process()
    else:
    	pro.start_process()
    return redirect("/")
# Metodo que toma las ultimas 10 muestras de la base de datos, calcula el promedio y lo retorna
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
	if cant == 10:
		tempavg=round(tempavg/cant,2)
		windavg=round(windavg/cant,2)
		humavg=round(humavg/cant,2)
		pressavg=round(pressavg/cant,2)
		return render_template('promedios.html',tempavg=tempavg ,humavg=humavg,windavg=windavg,pressavg=pressavg)
	else: 
		return render_template('promedios.html',tempavg="NaN" ,humavg="NaN",windavg="NaN",pressavg="NaN")

# Metodo que toma la ultima muestra de la base de datos y la devuelve
@app.route('/envivo')
def vivo():
	sample = db.get_sample()
	if len(sample):
		lasttemp = sample['temperature']
		lastwind = sample['windspeed']
		lasthum = sample['humidity']
		lastpress = sample['pressure']
		return render_template('envivo.html',temp=lasttemp , hum=lasthum, wind=lastwind, press=lastpress)	
	else:
		return render_template('envivo.html',temp="NaN" , hum="NaN", wind="NaN", press="NaN")

# Metodo que retorna la ultima muestra para la ruta /ultimo
@app.route('/ultimo')
def ultimo():
	sample = db.get_sample()
	if len(sample):

		lasttemp = sample['temperature']
		lastwind = sample['windspeed']
		lasthum = sample['humidity']
		lastpress = sample['pressure']
		return render_template('ultimo.html',temp=lasttemp , hum=lasthum, wind=lastwind, press=lastpress)	
	else:
		return render_template('ultimo.html',temp="NaN" , hum="NaN", wind="NaN", press="NaN")

@app.route('/lastjson/', methods = ['GET'])
def lastjson():
	sample = db.get_sample()
	return jsonify(sample)