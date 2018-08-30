from flask import Flask
from flask import render_template
from flask import request
from models import Samples
import random
import signal
from database import Database
import time 
# Metodo que genera los valores para las muestras
def getrand():
	temp= random.randrange(-5,40,1) + random.random()
	hum= random.randrange(40,100,1) + random.random()
	pressure= random.randrange(1000,1030,1) + random.random()
	wind= random.randrange(0,120,1) + random.random()
	return temp,hum,pressure,wind


class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)

	def exit_gracefully(self, signum, frame):
		self.kill_now = True

def main(session):
    killer = GracefulKiller()
    while(True):
        t,h,p,w = getrand()
        sample = Samples(temperature= round(t ,2), humidity = round(h,2), pressure = round(p,2), windspeed = round(w,2) )
        session.add(sample)
        session.commit()
        print("Muestra guardada ")
        time.sleep(1)
        # print x
        if killer.kill_now:
            session.close()
            break



if __name__ == '__main__':
   
    db = Database()
    session = db.get_session()
    main(session)