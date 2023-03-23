
from flask import Flask, jsonify, request
#from os import system
import pigpio

#system("sudo pigpiod")


app = Flask(__name__)

RED=17
GREEN=26
BLUE=22
BIG_FAN=6
LITTLE_FAN=5

BIG_FAN_RATE=0

pi=pigpio.pi();

### end point for leds ######
@app.route('/leds',methods=['POST','GET'])

def leds():
        pi.set_PWM_dutycycle(GREEN,request.args.get('g'))
        pi.set_PWM_dutycycle(BLUE,request.args.get('b'))
        pi.set_PWM_dutycycle(RED,request.args.get('r'))
        return ('done',200)




###end point for fan 1 ########
@app.route('/littlefan',methods=['POST','GET'])

def littlefan():
        out =255-int(request.args.get('speed'))
        pi.set_PWM_dutycycle(LITTLE_FAN,out)
        return (str(out),200)


####end point for fan 2 #########
@app.route('/bigfan',methods=['POST','GET'])

def bigfan():
        global BIG_FAN_RATE
        speed=request.args.get('speed')
        increment=request.args.get('increment')
        decrement=request.args.get('decrement')

        if (speed is not None and speed.isdigit()):
                BIG_FAN_RATE=int(speed)


        if (increment is not None and increment.isdigit()):
                BIG_FAN_RATE=BIG_FAN_RATE+int(increment)

        if(decrement is not None and decrement.isdigit()):
                BIG_FAN_RATE=BIG_FAN_RATE-int(decrement)


        if (BIG_FAN_RATE>255):
                BIG_FAN_RATE=255

        if (BIG_FAN_RATE<0):
                BIG_FAN_RATE=0

        pi.set_PWM_dutycycle(BIG_FAN,255-BIG_FAN_RATE)
        return ("{\"speed\":\"" + str(BIG_FAN_RATE) + "\"}",200)


if __name__ == '__main__':
        app.run(debug=False, host='0.0.0.0', port=5003)



