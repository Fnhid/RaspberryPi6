from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# 0.0.0.0:5000
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/on">LED ON</a>
        <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/<op>")
def led_op(op):
    print(op)
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>LED is now ON</p>
            <a href="/">Go main</a>
            <a href="/led/off">Wanna OFF?</a>
            
        '''
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
            <p>LED is now OFF</p>
            <a href="/">Go main</a>
            <a href="/led/on">Wanna ON?</a>
        '''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()