 #from gpiozero import LED
import socket
from time import sleep

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/activate', methods=['POST'])
def activate():
    device = request.form['device']
    print("activate request for device: {}".format(device))
    rainbow()

    return ''


def setup():
    requests.post('http://127.0.0.1:5000/connect',
                  data={'name': 'licht', 'ip': "127.0.0.1:5001"})

setup()

wecker_pin = 17
pc_pin = 27
wandlampe_pin = 22
coffee_pin = 10
blue_pin = 9
green_pin = 11
red_pin = 26

#wecker = LED(wecker_pin)
#pc = LED(pc_pin)
#wandlampe = LED(wandlampe_pin)
#coffee = LED(coffee_pin)

#blue = LED(blue_pin)
#red = LED(red_pin)
#green = LED(green_pin)


def hot():
    #red.on()
    #green.off()
    #blue.off()
    print("hot")


def well():
    #green.on()
    #blue.off()
    #red.off()
    print("well")


def cold():
    #blue.on()
    #red.off()
    #green.off()
    print("cold")


def rainbow():
    print("RAINBOW STARTED")
    #blue.on()
    #green.on()
    #red.on()
    sleep(5)
    #blue.off()
    #green.off()
    #red.off()
    #sleep(3)


#while True:
#    hot()
#    sleep(2)
#    well()
#    sleep(2)
#    cold()
#    sleep(2)
