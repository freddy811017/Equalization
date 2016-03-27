import cv2;
import numpy as np 


def calcAndDrawHist(image, color):    
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])    
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)    
    histImg = np.zeros([256,256,3], np.uint8)    
    hpt = int(0.9* 256);    
        
    for h in range(256):    
        intensity = int(hist[h]*hpt/maxVal)    
        cv2.line(histImg,(h,256), (h,256-intensity), color)    
            
    return histImg;   


img = cv2.imread('D:\\Freddy\\vision\\mp1.jpg',0)

histgray = calcAndDrawHist(img,[255,255,255])    
cv2.imshow("histgray", histgray)    
cv2.imshow("Image", img);
cv2.waitKey(0);


