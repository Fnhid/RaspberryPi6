import cv2

cap = cv2.VideoCapture(0) #카메라 장치 열기

if not cap.isOpened():
    print('Camera open failed')
    exit()

# 카메라 사진 찍기
ret, frame = cap.read()
cv2.imshow('frame', frame)
cv2.waitKey(0)



# 사용자 지원 해제
cap.release()
cv2.destroyAllWindows()