#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import time
import serial
from views import view

# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)
app.register_blueprint(view)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
