from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Samples
import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "tp2"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
    def init_samples(self, dict_match):
        """Generate the samples in the database
    
        Returns:
            [id of samples] --
        """
        session = self.get_session()
        sample = Samples()
        session.add(sample)
        session.commit()
        sample_id = int(sample.id)
        session.close()     
        return sample_id

    def get_sample(self):
        session = self.get_session()
        sample = session.query(Samples).order_by(Samples.id.desc()).first()
        session.close()
        return sample.serialize()

    def get_10_last_samples(self):
        session = self.get_session()
        samples = session.query(Samples).order_by(Samples.id.desc()).limit(10).all()
        session.close()        
        return [s.serialize() for s in samples]