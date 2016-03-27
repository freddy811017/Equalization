import cv2;
import numpy as np 

def calcAndDrawHist(img, color):    
    hist= cv2.calcHist([img], [0], None, [256], [0.0,255.0])    
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)    
    histImg = np.zeros([256,256,3], np.uint8)    
    hpt = int(0.9* 256);    
        
    for h in range(256):    
        intensity = int(hist[h]*hpt/maxVal)    
        cv2.line(histImg,(h,256), (h,256-intensity), color)            
    return histImg;  



img = cv2.imread('D:\\Freddy\\vision\\mp1a.jpg')
b,g,r= cv2.split(img)

bit = 256
high = len(b)
width = len(b[0])
sum = high*width

oldBdis = [0] * bit
oldGdis = [0] * bit
oldRdis = [0] * bit
oldBrat = [0] * bit
oldGrat = [0] * bit
oldRrat = [0] * bit
newBdis = [0] * bit
newGdis = [0] * bit
newRdis = [0] * bit

for i in range(0,high,1):
	for j in range(0,width,1):
		oldBdis[b[i][j]]+=1
		oldGdis[g[i][j]]+=1
		oldRdis[r[i][j]]+=1

	
for i in range(0,bit,1):
	oldBrat[i] = float(oldBdis[i])/sum
	oldGrat[i] = float(oldGdis[i])/sum
	oldRrat[i] = float(oldRdis[i])/sum



for i in range(0,bit,1):
	tempB = 0
	tempG = 0
	tempR = 0
	for j in range(0,i+1,1):
		tempB = tempB + oldBrat[j]
		tempG = tempG + oldGrat[j]
		tempR = tempR + oldRrat[j]
		
	newBdis[i] = round((bit-1) * tempB)
	newGdis[i] = round((bit-1) * tempG)
	newRdis[i] = round((bit-1) * tempR)
	
		
	
for i in range(0,high,1):
	for j in range(0,width,1):
		b[i][j] = newBdis[b[i][j]]
		g[i][j] = newGdis[g[i][j]]
		r[i][j] = newRdis[r[i][j]]


histImgB = calcAndDrawHist(b, [255, 0, 0])    
histImgG = calcAndDrawHist(g, [0, 255, 0])    
histImgR = calcAndDrawHist(r, [0, 0, 255])           
cv2.imshow("histImgB", histImgB)    
cv2.imshow("histImgG", histImgG)    
cv2.imshow("histImgR", histImgR)    

img = cv2.merge((b,g,r))
cv2.imshow('image',img);
cv2.imwrite('new.jpg',img);
cv2.waitKey(0);
cv2.destroyAllWindows();
