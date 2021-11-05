from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:mypass@localhost:3306/dbname")

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()
