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
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
# Ruta inicial
@app.route('/',methods=["GET"])

# Metodo inicial
def index():
	if not pro.is_running():
		pro.start_process()
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")
		print("Empezando process ")



	return average()

    
# Metodo que toma las ultimas 10 muestras de la base de datos, calcula el promedio y lo retorna
# @app.route('/promedios')
def average():
	tempavg = 0
	windavg = 0
	pressavg = 0
	humavg = 0
	samples = db.get_10_last_samples()  #Agarro las ultimas muestras 
	cant = len(samples)
	if cant>0:    				#verifico que haya al menos una muestra
		sample = samples[cant-1]
		lasttemp = sample['temperature']
		lastwind = sample['windspeed']
		lasthum = sample['humidity']
		lastpress = sample['pressure']
	else: #devuelvo valores no disponibles si no hay
		return render_template('index.html',tempavg="NaN" ,humavg="NaN",windavg="NaN",pressavg="NaN",lasttemp="NaN" ,lasthum="NaN", lastwind="NaN", lastpress="NaN")
	if cant==10:       #calculo promedio solo si hay 10 muestras.
		for i in samples:
			tempavg += i['temperature']
			windavg += i['windspeed']
			humavg += i['humidity']
			pressavg += i['pressure']
		tempavg=round(tempavg/cant,2)
		windavg=round(windavg/cant,2)
		humavg=round(humavg/cant,2)
		pressavg=round(pressavg/cant,2)
		return render_template('index.html',tempavg=tempavg ,humavg=humavg, windavg=windavg, pressavg=pressavg, lasttemp=lasttemp, lastpress=lastpress, lastwind=lastwind, lasthum=lasthum)
	else: 
		return render_template('index.html',tempavg="NaN" ,humavg="NaN",windavg="NaN",pressavg="NaN",lasttemp=lasttemp , lasthum=lasthum, lastwind=lastwind, lastpress=lastpress)

# Metodo que retorna la ultima muestra para la ruta /ultimo


@app.route('/avgjson/', methods = ['GET'])
def avgjson():
	tempavg = 0
	windavg = 0
	pressavg = 0
	humavg = 0
	temp = 0
	wind = 0
	hum = 0
	press = 0
	samples = db.get_10_last_samples()
	cant = len(samples)
	if (cant>0):
		for i in samples:
			tempavg += i['temperature']
			windavg += i['windspeed']
			humavg += i['humidity']
			pressavg += i['pressure']
		temp=samples[cant-1]['temperature']	
		wind = samples[cant-1]['windspeed']
		hum = samples[cant-1]['humidity']
		press = samples[cant-1]['pressure']
	if cant == 10:
		tempavg=round(tempavg/cant,2)
		windavg=round(windavg/cant,2)
		humavg=round(humavg/cant,2)
		pressavg=round(pressavg/cant,2)

	return jsonify(temperature = tempavg,
    				humidity = humavg,
    				pressure = pressavg,
    				windspeed = windavg,
    				lasttemp = temp,
    				lasthum = hum,
    				lastpress = press,
    				lastwind = wind)	