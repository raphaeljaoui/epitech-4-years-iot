from flask import Flask, request, jsonify
from flask_cors import CORS
import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)


@app.route('/light_sensor', methods=['POST'])
def light_sensor():
        result = request.json
        is_open = result["is_open"]
        light_sensor = result['light_sensor']
        time = result['time']

        print(is_open)
        print(light_sensor)
        print(is_open)
        print(time)
        
        test1("OJfqGEBS6iy8OTv6R7vu")

        return(result)
   


@app.route('/temp_humidity', methods=['POST'])
def temp_humidity():
    result = request.json
    value = result["value"]
    time = result['time']

    print(value)
    print(time)
    
    return(result)

@app.route('/fluid_sensor', methods=['POST'])
def fluid_sensor():
    result = request.json
    value = result["value"]
    time = result['time']
    color = result['color']
    quantity = result['quantity']

    print(value)
    print(time)
    print(quantity)
    print(color)
    
    return(result)





broker="thingsboard.cloud"   			    #host name
port=1883 					    #data listening port

def on_publish(client,userdata,result):             #create function for callback
    print("data published to thingsboard \n")
    pass

def test1(ACCESS_TOKEN):
    client1= paho.Client("control1")
    client1.on_publish = on_publish
    client1.username_pw_set(ACCESS_TOKEN)
    client1.connect(broker,port,keepalive=60)
    
    test = 0

    while test < 1:
        rand_humidity = (random.randint(0, 100))
        rand_temp = (random.randint(-20, 50))

        string1 = "\"Humidity\":" + str(rand_humidity) + ","
        string2 = "\"Temperature\":" + str(rand_temp)
        payload="{"
        payload+=string1
        payload+=string2
        payload+="}"
        ret= client1.publish("v1/devices/me/telemetry",payload)
        print("Please check LATEST TELEMETRY field of your device")
        print(payload)
        time.sleep(1)
        test +=1
