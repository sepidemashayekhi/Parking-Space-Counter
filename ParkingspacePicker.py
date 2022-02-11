from matplotlib import image
import numpy as np 
import cv2
import pickle

try:
    with open('CarParkPos','rb') as f :
        poslist=pickle.load(f)
except:
    poslist=[]


width,height=107,48
def mouseCallback(event,x,y,flag,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if event==cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(poslist):
            x1,y1=pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)
    with open('CarParkPos', 'wb') as f:
        pickle.dump(poslist, f)



while True:
    image=cv2.imread('carParkImg.png')
    for pos in poslist:
        cv2.rectangle(image,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)
    
    cv2.imshow("image",image)
    cv2.setMouseCallback("image",mouseCallback)
    if cv2.waitKey(1)==27:
        break
