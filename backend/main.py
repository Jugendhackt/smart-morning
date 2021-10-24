import json

from flask import Flask, request
from flask_cors import CORS, cross_origin
from threading import Thread
import requests
import datetime, time

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

known_devices = {}
wakeup_time = '12:00'
device_timings = {}
device_payloads = {}
enabled = True


def time_check():
    global device_payloads
    timestamp = 0
    while True:
        if enabled and datetime.datetime.now().strftime('%H:%M') > wakeup_time:
            if timestamp == 0:
                timestamp = time.time()

            try:
                for device in device_timings:
                    current_time = time.time() - timestamp

                    if not device_payloads.__contains__(device):
                        if float(device_timings[device]) * 60 < current_time:
                            send_post(device)
                            device_payloads[device] = True

            except RuntimeError:
                time_check()
        else:
            device_payloads = {}


def send_post(device):
    if known_devices.__contains__(device):
        requests.post('http://{}/activate'.format(known_devices[device]), data={'device': device})
        print("sending post req to {}".format(device))
    else:
        print("device {} not connected to system.".format(device))


def setup_app():
    t = Thread(target=time_check)
    t.start()


setup_app()


@app.route('/')
@cross_origin()
def index():
    return 'Smart-morning @ JH Rhein-Neckar'


@app.route('/send', methods=['POST'])
@cross_origin()
def receive_data():
    global wakeup_time, device_timings, enabled
    data = json.loads(request.data)

    wakeup_time = data['wakeup_time']
    devices_t = data['device_timings']
    for devices in devices_t:
        print(devices[0] + " " + devices[1])
        device_timings[devices[0]] = devices[1]
    print(device_timings)
    enabled = data['enabled']

    print("WTime: {} | dTimings: {} | enabled: {}".format(wakeup_time, device_timings, enabled))

    return ''


@app.route('/connect', methods=['POST'])
@cross_origin()
def connect():  # function to connect a device to the system
    global known_devices
    name = request.form['name']
    print("connected")

    if not known_devices.__contains__(name):
        known_devices[request.form['name']] = request.form['ip']

    print(known_devices)
    return ''


@app.route('/disconnect', methods=['POST'])
@cross_origin()
def disconnect():  # function to disconnect a device to the system
    global known_devices
    name = request.form['name']

    if known_devices.__contains__(name):
        del known_devices[name]

    print(known_devices)
    return ''
