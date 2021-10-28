import cv2
import time

cap = cv2.VideoCapture(0) #카메라 장치 열기
# xml 분류기 파일 로그
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourcc(four character code)
# DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # ('D', 'I', 'V', 'X')

# 동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    # 원본 이미지에 얼굴 위치 표시
    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    time.sleep(0.05)
    # 1000->1초, 10->0.01초
    if cv2.waitKey(10) == 13:
        break

# 사용자 지원 해제
cap.release()
cv2.destroyAllWindows()
