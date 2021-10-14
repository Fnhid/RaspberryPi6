import time
import picamera

path = '/home/pi/src6/06_multimedia'
nowtime = time.strftime("%Y%m%d_%H%M%S")
camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480)
    camera.start_preview()
    time.sleep(3)
    while True:
        
        hey = int(input("photo:1, video:2, exit:9 > "))
        if (hey == 1):
            print("Photo")
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3)
            camera.capture('%s/%s.jpg' % (path, nowtime))
        
        elif (hey == 2):
            print("Video")
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(3)
            camera.start_recording('%s/%s.h264' % (path, nowtime))
            time.sleep(5)
            camera.stop_recording()
        elif (hey == 9):
            exit()
        else:
            print("incorrect command")
        #camera.capture('%s/photo.jpg' % path)
        
finally:
    camera.stop_preview()