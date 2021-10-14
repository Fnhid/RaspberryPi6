# servo_motor.py
import RPi.GPIO as GPIO
import time

SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

#주파수 : 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5) # 0도

try:
    while True:
        val = input('1: 0도, 2: -90도, 3: +90도, 9: Exit >')
        if val == '1': 
            pwm.ChangeDutyCycle(7.5) # 0도
        elif val == '2': 
            pwm.ChangeDutyCycle(5) # -90도
        elif val == '3':
            pwm.ChangeDutyCycle(10) # +90도
        elif val == '9':
            break
        
finally: 
    pwm.stop()
    GPIO.cleanup()