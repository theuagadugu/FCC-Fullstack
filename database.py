import MySQLdb
import ssl
import os
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("DB_HOST")
user=os.getenv("DB_USERNAME")
password= os.getenv("DB_PASSWORD")
database= os.getenv("DB_DATABASE")




def load_jobs_from_db():
	"""
	Returns a list of jobs (list of dictionarys)
	"""
	with MySQLdb.connect(
		host= host,
		user=user,
		passwd= password,
		db= database,
		ssl={'ssl': {'cert_reqs': ssl.CERT_NONE}})	as connection:
		c=connection.cursor()
		c.execute("select * from jobs")
		result=list(c.fetchall())
		keys=[i[0] for i in c.description]
		return [dict(zip(keys,i)) for i in result]

def load_job_from_db(id):
	"""
	Returns a single dictionary with a row info
	"""
	with MySQLdb.connect(
		host= host,
		user=user,
		passwd= password,
		db= database,
		ssl={'ssl': {'cert_reqs': ssl.CERT_NONE}})	as connection:
		c=connection.cursor()
		c.execute(f"select * from jobs where id={id}")
		r=c.fetchall()
		keys=[i[0] for i in c.description]
		return [dict(zip(keys,i)) for i in r][0]


def get_applications_table_from_db():
	"""
	Crea la taula d'aplicacions. No executar mai!!!
	"""

	with MySQLdb.connect(
		host= host,
		user=user,
		passwd= password,
		db= database,
		ssl={'ssl': {'cert_reqs': ssl.CERT_NONE}})	as connection:
		c=connection.cursor()
		c.execute("select * from APPLICATIONS;")
		result=list(c.fetchall())
		return result


def add_application_to_db(job_id,data):
	with MySQLdb.connect(
		host= host,
		user=user,
		passwd= password,
		db= database,
		ssl={'ssl': {'cert_reqs': ssl.CERT_NONE}})	as connection:
		c=connection.cursor()
		sentence=f"INSERT INTO APPLICATIONS (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id}, '{data['full_name']}', '{data['email']}', '{data['linkedin']}', '{data['education']}', '{data['work_experience']}', '{data['url']}')"
		c.execute(sentence)
		result=connection.commit()
		print(result)


#ImmutableMultiDict([('full_name', 'nom complet2'), ('email', 'correu'), ('linkedin', 'linked'), ('education', 'educacio i tal '), ('work_experience', 'si he cotitzat'), ('url', 'url')])

if __name__ == '__main__':
	"""
	data={'full_name': 'nom complet3', 'email': 'correu', 'linkedin': 'linked', 'education': 'educacio i tal ', 'work_experience': 'si he cotitzat', 'url': 'url'}
	add_application_to_db(1,data)
	print("DATABASE:")
	print(get_applications_table_from_db())
	"""
	#print(os.getenv("HOST"))
	#print(load_jobs_from_db(), type(load_jobs_from_db()))
	#print(load_job_from_db(2))
