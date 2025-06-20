# Program To Read video
# and Extract Frames
import cv2
import numpy as np

#capture = cv2.VideoCapture("C:\\Users\\Francesco Morandotti\\OneDrive\\Documenti\\Phyton Scripts\\test env\\test.avi")
capture = cv2.VideoCapture("C:\\Users\\FMorandotti\\OneDrive\\Documenti\\Phyton Scripts\\test env\\test1.avi")



while True:
    ret, frame = capture.read()

    grey_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    grey_blur_frame = cv2.GaussianBlur( grey_frame , (15, 15) , 0)

    _, threshold = cv2.threshold(grey_blur_frame , 50 , 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours , key=lambda x: cv2.contourArea(x), reverse = True)

    for cnt in contours:
        ellipse = cv2.fitEllipse(cnt)
        #cv2.ellipse(grey_frame,ellipse, (255,255,255), 3)
        #cv2.drawContours(grey_frame , [cnt] , -1 , (255,255,255) , 2)
        break


    ellipse_area = ellipse[1][0]*ellipse[1][1]*3.1414
    if ( 5000 < ellipse_area < 80000):
        print(ellipse_area)
        cv2.ellipse(grey_frame,ellipse, (255,255,255), 3)
    else:
        print('fail')

    grey_frame_info = cv2.putText(grey_frame, 'ellipse[0][0]' , (20 , 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow("Frame" , threshold)
    cv2.imshow("Frame" , grey_frame_info)

    key = cv2.waitKey(3)
    if key == 27:
        break

   # https://www.youtube.com/watch?v=kbdbZFT9NQI&t=1s&ab_channel=Pysource