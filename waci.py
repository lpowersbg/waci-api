import flask
from flask import Flask, jsonify, request
import socket
import binascii

app = flask.Flask(__name__)
# Enable for Debug
app.config["DEBUG"] = False

mhost = '192.168.0.1'
mport = 7142

vhost = '10.51.201.100'
vport = 1000
on = b'<T0000681001000079>'
off = b'<T0000681000000078>'
status = b'<T0000681100000079>'
son = b'<F000068110100007a>'
soff = b'<F0000681100000079>'
goff = b'<F0000681000000078>'
ven = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def poweroff():
    mon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mon.connect((mhost, mport))
    message = b'\x01\x30\x2A\x30\x41\x30\x43\x02\x43\x32\x30\x33\x44\x36\x30\x30\x30\x34\x03\x1D\x0D'
    mon.send(message)

def poweron():
    mon = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mon.connect((mhost, mport))
    message = b'\x01\x30\x2A\x30\x41\x30\x43\x02\x43\x32\x30\x33\x44\x36\x30\x30\x30\x31\x03\x18\x0D'
    mon.send(message)

def venus(ope):
    ven.sendto(ope, (vhost, vport))
    return ven.recvfrom(1024)[0]


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
        poweroff()
    elif request.form['Param1'] == 'MonOn':
        # print('poweron')
        poweron()
    elif request.form['Param1'] == 'VenOn':
        # print('venuson')
        if venus(status) == soff:
            venus(on)
    elif request.form['Param1'] == 'VenRes':
        # print('venusres')
        if venus(status) == son:
            if venus(off) == goff:
                reply = venus(status)
                while reply != soff:
                    reply = venus(status)
                venus(on)
    elif request.form['Param1'] == 'VenOff':
        # print('venusoff')
        if venus(status) == son:
            venus(off)
    return "success"

# Enable for debug
# app.run(port='80',host='0.0.0.0')


