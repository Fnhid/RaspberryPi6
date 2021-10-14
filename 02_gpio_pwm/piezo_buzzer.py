#도레미파솔라시도 음 출력하기
import RPI.GPIO as GPIO
import time
BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUI)

pwm = GPIO.PWM(BUZZER_PIN, GPIO.OUT)

# 주파수 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle

melody = [262, 294, 330, 349, 392, 440, 494, 523]
try:
    for i in melody:
        pwm.ChangeFrequency(i)
        time.sleep(1)
finally:    
    pwm.stop()
    GPIO.cleanup()