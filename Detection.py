#pip install opencv-python
import cv2
import numpy as np

img_rgb=cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)

template=cv2.imread('opencv-template-for-matching.jpg',0)
w,h=template.shape[::-1]
res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
print(res)
threshold=0.8
loc=np.where(res>=threshold)
print(loc)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    #cv2.rectangle(img_gray,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

cv2.imshow('Detected',img_rgb)
#cv2.imshow('res',res)
#cv2.imshow('Detected',img_gray)
#cv2.imshow('GrayScaleing',img_gray)

if cv2.waitKey(1) & 0xFF==ord('q'):
    cv2.destroyAllWindows()
