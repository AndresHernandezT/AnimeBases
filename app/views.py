from app import app
from flask import render_template
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()


@app.route('/')
@app.route('/index')
def index():
	sql = "select * from animes"
	cur.execute(sql)
	resultados = cur.fetchall()
	return str(resultados[0])

@app.route('/adios')
def adios():
        return "No me quiero venir, senores homeros"
