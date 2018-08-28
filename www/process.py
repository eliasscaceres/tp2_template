from flask import Flask
from flask import render_template
from flask import request
from models import Samples
import random
import signal
from database import Database
import time 

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
        sample = Samples(temperature = t, humidity = h, pressure = p, windspeed = w )
        session.add(sample)
        session.commit()
        print("Muestra guardada ")
        time.sleep(1)
        # print x
        if killer.kill_now:
            session.close()
            break



if __name__ == '__main__':
    # if (len(sys.argv) != 4) or (sys.argv[1] == sys.argv[2]):
    #     sys.exit("Usage: python process.py id_team_1 id_team_2 id_match")
    # int_id_t1 = int(sys.argv[1])
    # int_id_t2 = int(sys.argv[2])
      # id_sample = 0    
    db = Database()
    session = db.get_session()
    # results = [ session.query(Sample).filter_by(id_sample=id_sample).first(), 
    #             session.query(Sample).filter_by(id_sample=id_sample).first()]
    main(session)
    

#app = Flask(__name__)
#@app.route('/')
#def index():
# return render_template('form.html')
#@app.route('/form')
#def action_form(nom=None):
# nom = request.args["nombre"]
# return render_template('response.html', name=nom)
#if __name__ == "__main__":
#  app.run(host='localhost', port=80)