from flask import Flask, render_template
import RPi.GPIO as GPIO
import cv2

SWITCH_PIN = 4
OLED_PIN = 5
RESISTER_PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN,GPIO.OUT)
GPIO.setup(OLED_PIN,GPIO.OUT)
GPIO.setup(RESISTER_PIN,GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("web.html")


@app.route("/home")
def home():
    return '''
        <p>HOME</p>
    '''

@app.route("/photo")
def photo():
    return '''
        <p>PHOTO</p>
    '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
