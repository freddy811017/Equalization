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



img = cv2.imread('D:\\Freddy\\vision\\mp1a.jpg')
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
Y, Cb, Cr= cv2.split(img)
	
histImgY = calcAndDrawHist(Y, [255, 0, 0])    
histImgCr = calcAndDrawHist(Cr, [0, 255, 0])    
histImgCb = calcAndDrawHist(Cb, [0, 0, 255])    

out = cv2.cvtColor(imghsv, cv2.COLOR_YCR_CB2BGR)

cv2.imshow("histImgY", histImgY)    
cv2.imshow("histImgCb", histImgCb)    
cv2.imshow("histImgCr", histImgCr)    
cv2.imshow("Image", out);
cv2.waitKey(0);
