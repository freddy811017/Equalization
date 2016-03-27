import cv2;
import numpy as np 
#顯示出直方圖的函式
def calcAndDrawHist(image, color):    
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])    
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)    
    histImg = np.zeros([256,256,3], np.uint8)    
    hpt = int(0.9* 256);    
        
    for h in range(256):    
        intensity = int(hist[h]*hpt/maxVal)    
        cv2.line(histImg,(h,256), (h,256-intensity), color)    
            
    return histImg;   


#讀取圖片進來
img = cv2.imread('D:\\Freddy\\vision\\mp1a.jpg')
#先將圖片轉成YCrCb　再個別分開
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
Y, Cb, Cr= cv2.split(img)
	
histImgY = calcAndDrawHist(Y, [255, 0, 0])    
histImgCr = calcAndDrawHist(Cr, [0, 255, 0])    
histImgCb = calcAndDrawHist(Cb, [0, 0, 255])      
#最後要將Y Cr Cb合併在一起
out = cv2.cvtColor(imghsv, cv2.COLOR_YCR_CB2BGR)

cv2.imshow("histImgY", histImgY)    
cv2.imshow("histImgCb", histImgCb)    
cv2.imshow("histImgCr", histImgCr)    
cv2.imshow("Image", out);
cv2.waitKey(0);

