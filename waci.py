import flask
from flask import request
import venus
import monwall

app = flask.Flask(__name__)
# Enable for Debug
app.config["DEBUG"] = False

@app.route('/rpc/', methods=['POST'])
def home():
    # Debug
    # print("success")
    # print(request.form['method'])
    # print(request.form['Param1'])
    # print(request.form['Param2'])
    # print(request.form['Param3'])
    # print(request.form['Param4'])
    if request.form['Param1'] == 'MonOff':
        # print('poweroff')
        monwall.monoff()
    elif request.form['Param1'] == 'MonOn':
        # print('poweron')
        monwall.monon()
    elif request.form['Param1'] == 'VenOn':
        # print('venuson')
        venus.venuson()
    elif request.form['Param1'] == 'VenRes':
        # print('venusres')
        venus.venusres()
    elif request.form['Param1'] == 'VenOff':
        # print('venusoff')
        venus.venusoff()
    return "success"

# Enable for debug
# app.run(port='80',host='0.0.0.0')


