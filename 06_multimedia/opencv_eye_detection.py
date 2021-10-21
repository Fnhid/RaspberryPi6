import cv2


face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

img = cv2.imread('./avengers.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray)


for(x, y, w, h) in faces:

    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # 얼굴에 검출된 영역 내부에서만 진행하기 위해 ROI 생성
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    # 눈 검출
    eyes = eye_cascade.detectMultiScale(roi_gray)
    # 눈 위치에 대한 좌표 정보 가져오기
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 