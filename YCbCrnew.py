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
imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
Y, Cr, Cb = cv2.split(imgYCrCb)


bit = 256
high = len(Y)
width = len(Y[0])
sum = high*width

oldYdis = [0] * bit
oldYrat = [0] * bit
newYdis = [0] * bit


for i in range(0,high,1):
	for j in range(0,width,1):
		oldYdis[Y[i][j]]+=1
	
for i in range(0,bit,1):
	oldYrat[i] = float(oldYdis[i])/sum

	
for i in range(0,bit,1):
	tempY = 0
	for j in range(0,i+1,1):
		tempY = tempY + oldYrat[j]
		
	newYdis[i] = round((bit-1) * tempY)
	
	
for i in range(0,high,1):
	for j in range(0,width,1):
		Y[i][j] = newYdis[Y[i][j]]

	
histImgY = calcAndDrawHist(Y, [255,0,0])    
histImgCr = calcAndDrawHist(Cr, [0,255,0])    
histImgCb = calcAndDrawHist(Cb, [0,0,255])    


imghsv = cv2.merge([Y, Cr, Cb])
out = cv2.cvtColor(imghsv, cv2.COLOR_YCR_CB2BGR)

   
cv2.imshow("histImgY", histImgY)    
cv2.imshow("histImgCr", histImgCr)    
cv2.imshow("histImgCb", histImgCb)    
cv2.imshow("Image", out);
cv2.imwrite('YCrCbnew.jpg',out);
cv2.waitKey(0);
cv2.destroyAllWindows();

