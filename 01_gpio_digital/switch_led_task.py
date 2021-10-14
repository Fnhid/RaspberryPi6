import RPi.GPIO as GPIO
import time
SWITCH_PINS = [6, 4, 5]
LED_PINS = [11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PINS, GPIO.OUT)  

def GGAMBBAK(pin): 

        val = GPIO.input(pin) # 누르지 않았을때 0, 눌렀을 때 1
        print(val)
        time.sleep(0.1)
        GPIO.output(pin + 5, val) # GPIO.HIGH = 1

try:
    while True:
        for i in SWITCH_PINS:
            GGAMBBAK(i)
finally:
    GPIO.cleanup()
    print('cleanup and exit')