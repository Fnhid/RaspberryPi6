import RPi.GPIO as GPIO
import time
j = 0
def LED_GGAMBBAK(LED_PIN):
    global j
    print(COLOR_LIST[j], "Led on")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2)
    print(COLOR_LIST[j], "Led off")
    GPIO.output(LED_PIN, GPIO.LOW)
    j += 1
LED_PIN = [4, 17, 27]
COLOR_LIST = ["RED", "YELLOW","GREEN"] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
for i in LED_PIN:
    LED_GGAMBBAK(i)
GPIO.cleanup()