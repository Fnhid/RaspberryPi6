import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
try:
    while True:
        inp = input("1:on, 0:off, 9:exit >")
        if inp == '0':
            GPIO.output(LED_PIN, GPIO.LOW)
            print("led off")
        elif inp == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("led on")
        elif inp == '9':
            break
finally:
    GPIO.cleanup()
    print("cleanup and exit")