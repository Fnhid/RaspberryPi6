import RPi.GPIO as GPIO
import Adafruit_DHT 
import time  
import threading # importing modules

sensor = Adafruit_DHT.DHT11
SEGMEMT_dec = 9
              # A B C D E F G
SEGMENT_PINS = [19,15,12,10,11,8,18]
DIGIT_PINS = [20,17,16,14]
LED_PIN = 26
SWITCH_PIN = 5
BUZZER_PIN = 3 
SENSOR_PIN = 27            # setting pins
GPIO.setmode(GPIO.BCM)     # set GPIO mode

GPIO.setup(SEGMEMT_dec, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)
for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)
pwm = GPIO.PWM(BUZZER_PIN, 262)      # setting up GPIO

#자릿수 제어 Pin : HIGH->OFF, LOW->ON
for digit in DIGIT_PINS:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, GPIO.HIGH)
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

class display(threading.Thread):    # display thread
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):                  # thread main
        print("display thread start. . . ", threading.currentThread().getName())
        
        def display(digit, number): # 자릿수, 숫자
                # 자리수에 해당하는 핀만 LOW로 설정
                
                    for i in range(4): # 0~3
                        if i + 1 == digit:
                            GPIO.output(DIGIT_PINS[i], GPIO.LOW)
                        else:
                            GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
        time.sleep(0.01)
        def temp():  #temperature를 받아 가공

            d = tem // 1000            
            c = (tem % 1000) // 100    
            b = ( tem % 100) // 10
            a = (tem % 10)
            if (ten >= 30): # 원래 37.5도로 설정하려 했으나, 37.5도까지 온도가 올라가지 않는 사유로 30도로 설정
                print("Danger! your tmp is "+ str(ten))         # 위험 온도 케이스
                pwm.start(10) # duty cycle
                GPIO.output(LED_PIN, GPIO.HIGH)
                time.sleep(1)
                pwm.stop()
                GPIO.output(LED_PIN, GPIO.LOW)
            else:
                print("Your tmp is " + str(ten))                # 정상 온도 케이스
            print(str(d) + str(c) + str(b) + str(a))            # pi에서의 확인용 print
            display(1, d)    
            display(2, c)
            display(3, b)
            display(4, a) # 4-digit 표시                                            
        
                    
    # 숫자 출력
    for i in range(7): #0~6
        GPIO.output(SEGMENT_PINS[i], data[number][i])
        while True:
            exc = GPIO.input(SWITCH_PIN) # Switch를 누르면 실행

            if(exc == 1):
    
                temp()
                            




                print("display thread end. . . ", threading.currentThread().getName())

class measure(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
    
        print("measure thread start ", threading.currentThread().getName())
        time.sleep(0.01)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, SENSOR_PIN) #온도 가져오기

        if humidity is not None and temperature is not None:
            global tem
            global ten
            tem = (int)(temperature * 10)
            ten = temperature
            print('mesaure : %d, %d' % (tem, ten))
        print("measure thread end ", threading.currentThread().getName())

print("main thread start")
t1 = measure("ms")
t1.start()      
t2 = display("dp")          
t2.start()                      

print("main thread end")

#finally:
#    GPIO.cleanup()
#    print('bye') 
