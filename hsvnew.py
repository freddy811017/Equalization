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
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imghsv)


bit = 256
high = len(v)
width = len(v[0])
sum = high*width

oldVdis = [0] * bit
oldVrat = [0] * bit
newVdis = [0] * bit


for i in range(0,high,1):
	for j in range(0,width,1):
		oldVdis[v[i][j]]+=1
	
for i in range(0,bit,1):
	oldVrat[i] = float(oldVdis[i])/sum

	
for i in range(0,bit,1):
	tempV = 0
	for j in range(0,i+1,1):
		tempV = tempV + oldVrat[j]
		
	newVdis[i] = round((bit-1) * tempV)
	
	
for i in range(0,high,1):
	for j in range(0,width,1):
		v[i][j] = newVdis[v[i][j]]

	
histImgH = calcAndDrawHist(h, [255,0,0])    
histImgS = calcAndDrawHist(s, [0,255,0])    
histImgV = calcAndDrawHist(v, [0,0,255])    


imghsv = cv2.merge([h, s, v])
out = cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR)
   
cv2.imshow("histImgH", histImgH)    
cv2.imshow("histImgS", histImgS)    
cv2.imshow("histImgV", histImgV)    
cv2.imshow("Image", out);
cv2.imwrite('hsvnew.jpg',out);
cv2.waitKey(0);
cv2.destroyAllWindows();

