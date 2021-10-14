import Rpi.GPIO as GPIO
import time

LED_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수 설정 : 50Hz
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0) # duty cycle 0~100

try:
    for i in range(3):
    #서서히 켜지게 하기
        for j in range(0, 101, 5): # start, end, step
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
    #서서히 꺼지게 하기
        for j in range(100, 0, -5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
finally:
    pwm.stop() # PWM 종료
    GPIO.cleanup()
    print("cleanup and exit")