#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import time
import serial

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_pi import Camera

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)

"""Instantiate UART module for Raspberry Pi"""
ser = serial.Serial(
    port='/dev/serial0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.5)

def send_thru_uart(to_send):
    """Helper function to send UART through Raspberry Pi GPIO to STM32"""
    ser.write(str.encode(to_send))
    ser.flushInput()
    ser.flushOutput()
    time.sleep(.5)
    
    timeout = time.time() + 2
    while True:
       ret = ser.readline()
       if ret != b'':
          return
       if time.time() > timeout:
          send_thru_uart(to_send)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/blue_on')
def blue_on():
    """Route to turn on the Blue LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    if(ser.isOpen() == False):
        ser.open()
    ser.reset_input_buffer()
    to_send = "LBO"

    send_thru_uart(to_send)
    return render_template('index.html')

@app.route('/blue_off')
def blue_off():
    """Route to turn off the Blue LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    if(ser.isOpen() == False):
        ser.open()
    ser.reset_input_buffer()
    to_send = "LBF"

    send_thru_uart(to_send)
    return render_template('index.html')

@app.route('/red_on')
def red_on():
    """Route to turn on the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    if(ser.isOpen() == False):
        ser.open()
    ser.reset_input_buffer()
    to_send = "LRO"

    send_thru_uart(to_send)
    return render_template('index.html')

@app.route('/red_off')
def red_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    if(ser.isOpen() == False):
        ser.open()
    ser.reset_input_buffer()
    to_send = "LRF"

    send_thru_uart(to_send)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
