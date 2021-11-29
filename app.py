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

TOKEN1 = "OJfqGEBS6iy8OTv6R7vu"
TOKEN2 = "Ox3aRPdHvqZAtbIw4P0W"
TOKEN3 = "xqP50CYO2yvjjRHXoEUT"


TOKEN4 = "KTEfpUvRGNk6oxkBoHd8"
TOKEN5 = "xWPqk1txZ8uNHgbLO6ZY"
TOKEN6 = "rhxMmG39ZWY4Rno0igwe"

TOKEN7="0z54NDIuYa7b8MNVX17C"
TOKEN8="itzjUhFcEH2J9kZVTqct"
TOKEN9="vHAIXeSYYMNUjSsfVSVS"


tabsensor = [{"light_intensity":10, "on_off":True, "light_statut": "day"}, {"light_intensity":15, "on_off":True, "light_statut": "day"}, {"light_intensity":20, "on_off":True, "light_statut": "day"}]


@app.route('/light_sensor', methods=['POST'])
def light_sensor():
        result = request.json
        is_open = result["is_open"]
        print(type(is_open))
        light_sensor = result['light_sensor']
        light_intensity = result['time']

        test = result['name']
        print("-----------------------------------------")
        print(test)
        print("-------------------------------------")

        if (is_open == True):
            print("OUI")

        print(light_sensor)
    
        if test == "1":
            tabsensor[0]["light_intensity"] = light_intensity;
            tabsensor[0]["on_off"] = light_sensor;
            tabsensor[0]["light_statut"] = is_open;
        if test == "2":
            tabsensor[1]["light_intensity"] = light_intensity;
            tabsensor[1]["on_off"] = light_sensor;
            tabsensor[1]["light_statut"] = is_open;
        if test == "3":
            tabsensor[2]["light_intensity"] = light_intensity;
            tabsensor[2]["on_off"] = light_sensor;
            tabsensor[2]["light_statut"] = is_open;
        light_sensor_call(TOKEN6, tabsensor[2]["light_statut"], tabsensor[2]["on_off"], tabsensor[2]["light_intensity"])
        light_sensor_call(TOKEN5, tabsensor[1]["light_statut"], tabsensor[1]["on_off"], tabsensor[1]["light_intensity"])
        light_sensor_call(TOKEN4, tabsensor[0]["light_statut"], tabsensor[0]["on_off"], tabsensor[0]["light_intensity"])

        return(result)


@app.route('/temp_humidity', methods=['POST'])
def temp_humidity():
    result = request.json
    value = result["value"]
    time = result['time']

    print(value)
    print(time)
    
    temp_humidity_call(TOKEN1)
    temp_humidity_call(TOKEN2)
    temp_humidity_call(TOKEN3)
    temp_humidity_call(TOKEN4)
    return(result)

@app.route('/fluid_sensor', methods=['POST'])
def fluid_sensor():
    result = request.json
    Substance = result["value"]
    time = result['time']
    INK = result['color']
    Consume = result['quantity']

    print(Substance)
    print(time)
    print(Consume)
    print(INK)
    fluid_sensor(TOKEN7, Substance, Consume, INK)
    fluid_sensor(TOKEN8, Substance, Consume, INK)
    fluid_sensor(TOKEN9, Substance, Consume, INK)
    return(result)





broker="thingsboard.cloud"
port=1883

def on_publish(client,userdata,result):
    print("data published to thingsboard \n")
    pass

def temp_humidity_call(ACCESS_TOKEN):
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



def light_sensor_call(ACCESS_TOKEN, light_statut, on_off, light_intensity):
    client1= paho.Client("control1")
    client1.on_publish = on_publish
    client1.username_pw_set(ACCESS_TOKEN)
    client1.connect(broker,port,keepalive=60)
    test = 0


    print(light_intensity)
    print("on_off : ", on_off)
    print("light status :", light_statut)

    string1 = "\"light_intensity\":\"" + str(light_intensity) + "\","
    string2 = "\"on_off\":" + str(on_off) + ","
    string3 =  "\"light_statut\":" + str(light_statut)
    while test < 1:
        
        payload="{"
        payload+=string1
        payload+=string2
        payload+=string3
        payload+="}"

        ret= client1.publish("v1/devices/me/telemetry",payload)
        print(payload)
        print("Please check LATEST TELEMETRY field of your device")
        time.sleep(1)
        test +=1


def fluid_sensor(ACCESS_TOKEN, Substance, Consume, INK):
    client1= paho.Client("control1")
    client1.on_publish = on_publish
    client1.username_pw_set(ACCESS_TOKEN)
    client1.connect(broker,port,keepalive=60)
    test = 0


    print("substance =", Substance)
    print("CONSUME", Consume)
    print("INK", INK)

    string1 = "\"Substance\":\"" + str(Substance) + "\","
    string2 = "\"Consume\":" + str(Consume) + ","
    string3 =  "\"INK\":\"" + str(INK) + "\""
    while test < 1:
        
        payload="{"
        payload+=string1
        payload+=string2
        payload+=string3
        payload+="}"

        ret= client1.publish("v1/devices/me/telemetry",payload)
        print(payload)
        print("Please check LATEST TELEMETRY field of your device")
        time.sleep(1)
        test +=1
