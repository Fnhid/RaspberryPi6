from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
RED_LED_PIN = 22
BLUE_LED_PIN = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

# 0.0.0.0:5000
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<boo>")
def led_op(color, boo):
    print(color + " " + boo)

    if color == "red":
        if(boo == "on"):
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return '''
                <p>Red LED is now ON</p>
                <a href="/">Go main</a>
            '''
        elif(boo == "off"):
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return '''
                <p>Red LED is now OFF</p>
                <a href="/">Go main</a>
            '''
    elif color == "blue":
        if(boo == "on"):
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
            return '''
                <p>Blue LED is now ON</p>
                <a href="/">Go main</a>
            '''
        elif(boo == "off"):
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
            return '''
                <p>Blue LED is now OFF</p>
                <a href="/">Go main</a>
            '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()