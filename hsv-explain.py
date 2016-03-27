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


#把圖片讀取進來
img = cv2.imread('D:\\Freddy\\vision\\mp1a.jpg')
#先將圖片轉換成HSV　再把HSV分開來
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imghsv)
	
histImgH = calcAndDrawHist(h, [255,0,0])    
histImgS = calcAndDrawHist(s, [0,255,0])    
histImgV = calcAndDrawHist(v, [0,0,255])    
#分開後最後再把HSV合併在一起
out = cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR)
#印出HSV個別直方圖   
cv2.imshow("histImgH", histImgH)    
cv2.imshow("histImgS", histImgS)    
cv2.imshow("histImgV", histImgV)    
cv2.imshow("Image", out);
cv2.waitKey(0);

