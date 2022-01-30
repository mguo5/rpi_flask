from flask import Blueprint, render_template, session, abort, Response
import time
import serial
import os
from pi_serial import uart_communicate

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera_pi import Camera

view = Blueprint('view', __name__)

@view.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@view.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@view.route('/blue_on')
def blue_on():
    """Route to turn on the Blue LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    """Instantiate UART module for Raspberry Pi"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LBO"
    uart.send_thru_uart(to_send)
    print("Blue_on")
    return ("nothing")
    #return render_template('index.html')

@view.route('/blue_off')
def blue_off():
    """Route to turn off the Blue LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LBF"
    uart.send_thru_uart(to_send)
    print("Blue_off")
    return ("nothing")
    #return render_template('index.html')

@view.route('/red_on')
def red_on():
    """Route to turn on the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LRO"
    uart.send_thru_uart(to_send)
    print("Red_on")
    return ("nothing")
    #return render_template('index.html')

@view.route('/red_off')
def red_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LRF"
    uart.send_thru_uart(to_send)
    print("Red_off")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/orange_on')
def orange_on():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LOO"
    uart.send_thru_uart(to_send)
    print("Orange_on")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/orange_off')
def orange_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LOF"
    uart.send_thru_uart(to_send)
    print("Orange_off")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/green_on')
def green_on():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LGO"
    uart.send_thru_uart(to_send)
    print("Green_on")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/green_off')
def green_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "LGF"
    uart.send_thru_uart(to_send)
    print("Green_off")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/porta_on')
def porta_on():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "GAO"
    uart.send_thru_uart(to_send)
    print("Porta_on")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/porta_off')
def porta_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "GAF"
    uart.send_thru_uart(to_send)
    print("Porta_off")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/portb_on')
def portb_on():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "GBO"
    uart.send_thru_uart(to_send)
    print("Portb_on")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/portb_off')
def portb_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "GBF"
    uart.send_thru_uart(to_send)
    print("Portb_off")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/portc_on')
def portc_on():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "GCO"
    uart.send_thru_uart(to_send)
    print("Portc_on")
    return ("nothing")
    #return render_template('index.html')
    
@view.route('/portc_off')
def portc_off():
    """Route to turn off the Red LED. TODO: put functionality as a button onClick method to avoid reloading page"""
    uart = uart_communicate()
    if(uart.ser.isOpen() == False):
        uart.ser.open()
    uart.ser.reset_input_buffer()
    to_send = "GCF"
    uart.send_thru_uart(to_send)
    print("Portc_off")
    return ("nothing")
    #return render_template('index.html')
