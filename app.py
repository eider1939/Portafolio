import os
from flask import Flask
from flask import render_template, request, redirect, session
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/img/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('templates/img/'),imagen)

@app.route('/css/<archivocss>')
def css_link(archivocss):
    return send_from_directory(os.path.join('/css'),archivocss)

if __name__=='__main__':
    app.run(debug=True)