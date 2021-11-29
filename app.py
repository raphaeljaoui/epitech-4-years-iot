from flask import Flask, request, jsonify
from flask_cors import CORS

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
