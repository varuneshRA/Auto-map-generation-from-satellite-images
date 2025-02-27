import cv2

from matplotlib import pyplot as plt
img = cv2.imread('InputDir/img3.png',0)

# Apply global (simple) thresholding on image
ret1,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

# Apply Otsu's thresholding on image
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Apply Otsu's thresholding after Gaussian filtering
blur = cv2.GaussianBlur(img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

titles = ['Original Image','Global Thresholding (v=127)',"Otsu's Thresholding",'Gaussian Filter + Otsu']
images = [img,th1,th2,th3]

for i in range(4):
   plt.subplot(2,2,i+1)
   plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.axis("off")
plt.show()