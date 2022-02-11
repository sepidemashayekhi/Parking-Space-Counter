import cv2
import cvzone
import pickle
import numpy as np 
width,height=107,48
with open('CarParkPos','rb') as f :
        posList=pickle.load(f)


parkingVideo=cv2.VideoCapture('carPark.mp4')

while True:
    _,frame=parkingVideo.read()
    if parkingVideo.get(cv2.CAP_PROP_POS_FRAMES)==parkingVideo.get(cv2.CAP_PROP_FRAME_COUNT):
        parkingVideo.set(cv2.CAP_PROP_POS_FRAMES,0)
    for pos in posList:
        cv2.rectangle(frame,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    
    cv2.imshow("frame",frame)
    cv2.waitKey(1)