# py -3.8 -m pip install autopy가 3.8까지밖에 지원 안함

import cv2
import numpy as np
import hand_traking_module as htm
import time
import autopy

################################
wCam,hCam =640,480
frameR = 100
################################

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

cTime = 0
pTime = 0

detector = htm.handDetector(maxHands=1)

wScr,hScr = autopy.screen.size() 

while True:
    try:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList,bbox = detector.findPosition(img)

        if len(lmList)!=0:
            x0,y0 = lmList[4][1:]
            x1,y1 = lmList[8][1:]
            x2,y2 = lmList[12][1:]
            x3,y3 = lmList[16][1:]
            x4,y4 = lmList[20][1:]

            # print(x1,y1,x2,y2)

            fingers = detector.fingersUp()
            # print(fingers)

            if fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 1  and fingers[3] == 1  and fingers[4] == 1:

                cv2.circle(img,(x1,y1),15,(0,0,255),cv2.FILLED)


            if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:
                pass




        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)
        
    except ValueError:continue