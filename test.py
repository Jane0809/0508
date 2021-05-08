import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

@app.route('/<parm>', methods = ['GET'])
def index(parm):
    
    return_string = "1"
    
    if parm == "1":
        GPIO.output(25, GPIO.HIGH)
        return 'LED_ON'
    else:
        GPIO.output(25, GPIO.LOW)
        return 'LED_OFF'
    return return_string

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(25, GPIO.OUT)
    app.run()