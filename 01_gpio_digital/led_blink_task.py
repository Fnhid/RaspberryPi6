import RPi.GPIO as GPIO
import time
def LED_GGAMBBAK(LED_PIN):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED_PIN, GPIO.LOW)
LED_PIN = [4, 17, 27]
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

for i in LED_PIN:
    LED_GGAMBBAK(i)
GPIO.cleanup()