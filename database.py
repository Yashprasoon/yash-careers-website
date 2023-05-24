import sqlalchemy
from sqlalchemy import create_engine,text
import os
url = os.environ['DB_CONNECTION_STRING']

engine = create_engine(url, connect_args={"ssl":{"ssl_ca":"/etc/ssl/cert.pem"}},echo=True)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  
    jobs =[]
    result_all = result.all()
    column_names = result.keys()
    
    for row in result_all:
      jobs.append(dict(zip(column_names,row)))
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id ={id}"))
    rows = result.all()
    print(rows) 
    column_names = result.keys()
    
    if len(rows) == 0:
      return None
    else:
      return(dict(zip(column_names,rows[0])))
load_job_from_db(1)