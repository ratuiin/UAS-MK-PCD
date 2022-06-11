# Import Packet
import cv2
import numpy as np

# Membaca file gambar yang berda dalam folder yang sama dengan file
image = cv2.imread("iqbaal.jpeg")
# Menampilkan data piksel citra
print('Image', image)

# Menampilkan Citra Original
cv2.imshow("Gambar Original", image)

# Menampilkan citra grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale ", gray)

# Menampilkan citra HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Picture", hsv)

# Median Filter
img_median = cv2.medianBlur(hsv, 5) # Add median filter to image
cv2.imshow('Median Filter 0', img_median)

# Applying Otsu in Green Channel
img = img_median[:,:,1] #get the green channel
th, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('Otsu Tresholding', img)

# Opening
kernel = np.ones((7,7),np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imshow('Opening', opening)

# Aritmatic AND Operation
dest_and = cv2.bitwise_and(image, image, mask = opening)
cv2.imshow('Bitwise And', dest_and)

cv2.waitKey(0)
cv2.destroyAllWindows()