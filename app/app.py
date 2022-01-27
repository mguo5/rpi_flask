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

import views

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
