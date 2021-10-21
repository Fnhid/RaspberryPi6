import cv2
import time

cap = cv2.VideoCapture(0) #카메라 장치 열기

if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourcc(four character code)
# DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # ('D', 'I', 'V', 'X')

out = cv2.VideoWriter('output.avi', fourcc, 30, (640, 480))

# 동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame, 50, 100)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge', edge)
    time.sleep(0.05)
    # 1000->1초, 10->0.01초
    if cv2.waitKey(10) == 13:
        break


    



# 사용자 지원 해제
cap.release()
out.release()
cv2.destroyAllWindows()
