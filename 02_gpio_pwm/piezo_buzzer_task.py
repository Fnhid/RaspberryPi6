import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)


pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [262 ,294 ,330 ,392 ,440]
def do(tm):
    pwm.ChangeFrequency(melody[0])
    time.sleep(tm)
def rae(tm):
    pwm.ChangeFrequency(melody[1])
    time.sleep(tm)
def mi(tm):
    pwm.ChangeFrequency(melody[2])
    time.sleep(tm)
def sol(tm):
    pwm.ChangeFrequency(melody[3])
    time.sleep(tm)
def ra(tm):
    pwm.ChangeFrequency(melody[4])
    time.sleep(tm)

do(1000)

    