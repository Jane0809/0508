import os
import glob
import time
from flask import Flask
from flask import request

app = Flask(__name__)
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_device_file():
    f = open(device_file,'r')
    lines = f.readlines()
    f.close()
    return lines
@app.route('/',methods = ['GET'])
    
def parse_temperature():
    lines = read_device_file()

    while lines[0].strip()[-3:] !='YES':
        time.sleep(0.1)
        lines = read_device_file()

    equals_pos = lines[1].find('t=')

    if equals_pos!= -1:
        temperature_string=lines[1][equals_pos+2:]
        temperature_c = float(temperature_string)/ 1000.0
        temperature_f = temperature_c * 9.0 /5.0 + 32.0
        return str(temperature_c)


if __name__== '__main__':
    app.run()