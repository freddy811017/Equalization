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

imggray = cv2.imread('D:\\Freddy\\vision\\mp1.jpg',0)

bit = 256
high = len(imggray)
width = len(imggray[0])
sum = high*width
oldimggraydis = [0] * bit
oldimggrayrat = [0] * bit
newimggraydis = [0] * bit


for i in range(0,high,1):
	for j in range(0,width,1):
		oldimggraydis[imggray[i][j]]+=1
		
for i in range(0,bit,1):
	oldimggrayrat[i] = float(oldimggraydis[i])/sum
	
for i in range(0,bit,1):
	tempgray = 0

	for j in range(0,i+1,1):
		tempgray = tempgray + oldimggrayrat[j]

	newimggraydis[i] = round((bit-1) * tempgray)

		
for i in range(0,high,1):
	for j in range(0,width,1):
		imggray[i][j] = newimggraydis[imggray[i][j]]

histgray = calcAndDrawHist(imggray,[255,255,255])    
cv2.imshow("histgray", histgray)    
cv2.imshow("Image", imggray);
cv2.waitKey(0);
cv2.destroyAllWindows();


