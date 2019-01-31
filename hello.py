from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/on/')
def hello(nbr=nbr):
    return render_template('on.html', nbr=nbr)

import RPi.GPIO as GPIO
import time

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#initialisation de la broche en mode "sortie"
#⚠️ Le nombre passé en paramètre correspond au numéro de GPIO et non au numéro de la broche.
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


@app.route('/on/')
@app.route('/on/<nbr>')
def on(nbr):
    if nbr == '1':
        GPIO.output(14, GPIO.HIGH)
    elif nbr == '2':
        GPIO.output(15, GPIO.HIGH)
    return render_template('on.html', nbr=nbr)

@app.route('/off/')
@app.route('/off/<nbr>')
def off(nbr):
    if nbr == '1':
        GPIO.output(14, GPIO.LOW)
    elif nbr == '2':
        GPIO.output(15, GPIO.LOW)
    return render_template('on.html', nbr=nbr)
