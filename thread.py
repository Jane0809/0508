import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import threading
import time

app = Flask(__name__)


def job():
    global var
    
    while 1==1:
        if var == 2:
            break
        GPIO.output(25, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(25, GPIO.LOW)
        time.sleep(1)


@app.route('/', methods = ['GET'])

def index():
    global var
    my_led_status = request.args.get('led_status')
 
    
    if my_led_status == "0":
        var = 2
        GPIO.output(25, GPIO.LOW)
        return 'LED_OFF'
    elif my_led_status == "1":
        var = 2
        GPIO.output(25, GPIO.HIGH)
        return 'LED_ON'
    elif my_led_status == "2":
        var = 1
        t = threading.Thread(target = job)
        t.start()
        return "start"
    elif my_led_status == "3":
        var = 2
        return "stop"

if __name__ == '__main__':
    global var
    var = 1
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    app.run()
