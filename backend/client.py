from gpiozero import LED,PWMLED
import socket
from time import sleep

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/activate', methods=['POST'])
def activate():
    device = request.form['device']
    print("activate request for device: {}".format(device))
    
    if device == "licht":
        wandlampe.on()
    elif device == "pc":
        pc.on()
    elif device == "kaffeemaschine":
        coffee.on()
    elif device == "heizung":
        heizung()
    elif device == "rollläden":
        curtain_up(0.575)

    return ''


@app.route('/deactivate', methods=['POST'])
def deactivate():
    device = request.form['device']
    
    if device == "licht":
        wandlampe.off()
    elif device == "pc":
        pc.off()
    elif device == "kaffeemaschine":
        coffee.off()
    elif device == "heizung":
        red.off()
        green.off()
        blue.off()
   
    return ''

def setup():
    requests.post('http://192.168.4.131:5000/connect',
                  data={'name': 'licht', 'ip': "192.168.4.131:5001"})
    requests.post('http://192.168.4.131:5000/connect',
                  data={'name': 'pc', 'ip': "192.168.4.131:5001"})
    requests.post('http://192.168.4.131:5000/connect',
                  data={'name': 'kaffeemaschine', 'ip': "192.168.4.131:5001"})
    requests.post('http://192.168.4.131:5000/connect',
                  data={'name': 'heizung', 'ip': "192.168.4.131:5001"})
    requests.post('http://192.168.4.131:5000/connect',
                  data={'name': 'rollläden', 'ip': "192.168.4.131:5001"})

setup()

wecker_pin = 17
pc_pin = 27
wandlampe_pin = 22
coffee_pin = 10
curtain_pin = 12

blue_pin = 9
green_pin = 11
red_pin = 26

wecker = LED(wecker_pin)
pc = LED(pc_pin)
wandlampe = LED(wandlampe_pin)
coffee = LED(coffee_pin)
curtain = PWMLED (curtain_pin)

blue = LED(blue_pin)
red = LED(red_pin)
green = LED(green_pin)


def heizung():
    cold()
    sleep(2)
    well()
    sleep(2)
    hot()
    sleep(2)
    
    
def curtain_up(sec) :
    curtain.value = 1
    sleep (0.16)
    curtain.value = 0.2
    sleep (sec)
    curtain.value = 0
    print("curtains up for {} seconds!".format(sec))
    



def hot():
    red.on()
    green.off()
    blue.off()
    print("hot")


def well():
    green.on()
    blue.off()
    red.off()
    print("well")


def cold():
    blue.on()
    red.off()
    green.off()
    print("cold")

#def rainbow():
#    print("RAINBOW STARTED")
#    blue.on()
#    green.on()
#    red.on()
#    sleep(5)
#    blue.off()
#    green.off()
#    red.off()
#    sleep(3)


#while True:
#    hot()
#    sleep(2)
#    well()
#    sleep(2)
#    cold()
#    sleep(2)
