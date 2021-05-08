import RPi.GPIO as GPIO
from flask import Flask
from flask import request
import time
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    
    my_led_status = request.args.get('value')
    
    if my_led_status == "0":
        GPIO.output(25, GPIO.LOW)
        return 'LED_OFF'
    elif my_led_status == "1":
        GPIO.output(25, GPIO.HIGH)
        return 'LED_ON'
    else:
        for i in range(5):
            GPIO.output(25, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(25, GPIO.LOW)
            time.sleep(1)
        return 'LED_string'
    return my_led_status

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    app.run()
