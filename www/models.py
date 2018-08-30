import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Clase correspondienta a una muestra, que tiene como atributos las distintas variables climaticas
class Samples(Base):
    __tablename__ = 'samples'
    id=Column(Integer, primary_key=True)
    temperature=Column('temperature', Float)
    humidity=Column('humidity', Float)
    pressure=Column('pressure', Float)
    windspeed=Column('windspeed', Float)
    
    def serialize(self):
    		return {
    				'id' : self.id,
    				'temperature' : self.temperature,
    				'humidity' : self.humidity,
    				'pressure' : self.pressure,
    				'windspeed' : self.windspeed,

    		}
 