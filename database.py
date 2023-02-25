import MySQLdb
import ssl
import os
from dotenv import load_dotenv

load_dotenv()
host= os.getenv("HOST")
user=os.getenv("USERNAME")
passwd= os.getenv("PASSWORD")
db= os.getenv("DATABASE")

def load_jobs_from_db():
	load_dotenv()
	connection = MySQLdb.connect(
  host= host,
  user=user,
  passwd= password,
  db= database,
  ssl={'ssl': {'cert_reqs': ssl.CERT_NONE}}
  
)	
	c=connection.cursor()
	c.execute("select * from jobs")
	result=list(c.fetchall())
	keys=[i[0] for i in c.description]
	a=[dict(zip(keys,i)) for i in result]
	return [dict(zip(keys,i)) for i in result]

if __name__ == '__main__':
	print(os.getenv("HOST"))
	print(load_jobs(), type(load_jobs()))