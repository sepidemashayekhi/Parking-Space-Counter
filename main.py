import cv2
import cvzone
import pickle
import numpy as np

width,height=107,48
with open('CarParkPos','rb') as f :
        posList=pickle.load(f)

def checkParkingSpace(imgPro):
    spaceCounter = 0
    for pos in posList:
        x,y=pos
        imgCrop=imgPro[y:y+height,x:x+width]
        count=cv2.countNonZero(imgCrop)
        # cv2.imshow(str(x),imgCrop)
        if count < 900:

            color = (0, 255, 0)
            thickness = 5
            spaceCounter += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(frame,pos,(pos[0]+width,pos[1]+height),color,thickness)
        cvzone.putTextRect(frame, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)
        cvzone.putTextRect(frame, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                           thickness=5, offset=20, colorR=(0,200,0))

parkingVideo=cv2.VideoCapture('carPark.mp4')

while True:
    _,frame=parkingVideo.read()
    if parkingVideo.get(cv2.CAP_PROP_POS_FRAMES)==parkingVideo.get(cv2.CAP_PROP_FRAME_COUNT):
        parkingVideo.set(cv2.CAP_PROP_POS_FRAMES,0)
    imgGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.GaussianBlur(imgGray,(3,3),1)
    imgThreshold=cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY_INV,25,16)
    imgMedian=cv2.medianBlur(imgThreshold,5)
    kernel=np.ones((3,3),np.int8)
    imgDilate=cv2.dilate(imgMedian,kernel,iterations=1)
    

    checkParkingSpace(imgDilate)
 
        
    
    cv2.imshow("frame",frame)
    # cv2.imshow("thresh",imgDilate)

    if cv2.waitKey(1)==27:
        break
