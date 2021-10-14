from lcd import drivers
import time
import datetime
import Adafruit_DHT
import RPi.GPIO as GPIO
sensor = Adafruit_DHT.DHT11
DHT_PIN = 25


display = drivers.Lcd()

try:
   
    while True:
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        print(now.strftime("%x %X"))
        print('%.1f*C, %.1f%%' % (t, h))
        display.lcd_display_string(now.strftime("%x%X"), 1)
        time.sleep(0.1)
        if h is not None and t is not None:
            display.lcd_display_string('%.1f*C, %.1f%%' % (t, h), 2)
        time.sleep(0.1)

finally:
    display.lcd_clear()
    GPIO.cleanup()
