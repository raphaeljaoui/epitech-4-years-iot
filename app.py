from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    return("NIQUE TA MERE")

    
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    print("ajisojao")
    print(request_data)

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['python']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][0]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


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
def temp_humidity():
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
