from flask import Flask, render_template
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
    return render_template("led2.html")

@app.route("/led/<boo>/<color>")
def led_op(boo, color):
    print(color + " " + boo)

    if color == "red":
        if(boo == "on"):
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return 'RED LED ON'
        elif(boo == "off"):
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return 'RED LED OFF'
    elif color == "blue":
        if(boo == "on"):
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
            return 'BLUE LED ON'
        elif(boo == "off"):
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
            return 'BLUE LED OFF'

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()