from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into animes (nombre,cant_capitulos,tipo,autor_id,estudio_id) values ('Death Note','38','Anime','1','1') returning id;
"""
cur.execute(sql)

conn.commit()
cur.close()
conn.close()
