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

　#讀取圖片  第二個參數若為0　代表為灰階
img = cv2.imread('D:\\Freddy\\vision\\mp1.jpg',0)
　#利用上面的函式去畫出直方圖
histgray = calcAndDrawHist(img,[255,255,255])    
　#顯示出直方圖與原始圖
cv2.imshow("histgray", histgray)    
cv2.imshow("Image", img);
cv2.waitKey(0);


