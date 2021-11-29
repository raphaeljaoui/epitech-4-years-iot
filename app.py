from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/light_sensor', methods=['POST'])
def light_sensor():
    result = request.form
    is_open = result["is_open"]
    light_sensor = result['light_sensor']
    time = result['time']

    print(light_sensor)
    print(is_open)
    print(time)
    
    return(result)


@app.route('/temp_humidity', methods=['POST'])
def temp_humidity():
    result = request.form
    value = result["value"]
    time = result['time']

    print(value)
    print(time)
    
    return(result)

@app.route('/fluid_sensor', methods=['POST'])
def fluid_sensor():
    result = request.form
    value = result["value"]
    time = result['time']
    color = result['color']
    quantity = result['quantity']

    print(value)
    print(time)
    print(quantity)
    print(color)
    
    return(result)
