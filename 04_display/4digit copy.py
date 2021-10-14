import RPi.GPIO as GPIO
import time  
              # A B C D E F G
SEGMENT_PINS = [19,15,12,10,11,8,18]
DIGIT_PINS = [20,17,16,14]
GPIO.setmode(GPIO.BCM)

for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

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
tem = 30
try:
    while True:

        d = tem // 1000            
        c = (tem % 1000) // 100    
        b = ( tem % 100) // 10
        a = (tem % 10)
        arr = [d, c, b, a]                 
        for i in range(4): # 0~3
        
            if i + 1 == digit:
                GPIO.output(DIGIT_PINS[i], GPIO.LOW)
            
            else:
                GPIO.output(DIGIT_PINS[i], GPIO.HIGH)
                
        for i in range(7): #0~6
        
            for j in arr:
                GPIO.output(SEGMENT_PINS[i], data[j][i])     # display 과정  

finally:
    GPIO.cleanup()
    print('bye')