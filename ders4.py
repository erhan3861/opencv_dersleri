import cv2

img = cv2.imread("resim.jpg") # resim dosyasını okur ve img değişkenine atar

resized = cv2.resize(img, (300, 300)) # 300x300 boyutuna getir
cv2.imshow("Kirpilmis", resized) # kırpılmış resmi ekranda göster


# crop = img[0:200, 100:300] # Matris dilimleme ile belirli alanı al
# cv2.imshow("Kirpilmis", crop) # kırpılmış resmi ekranda göster


cv2.waitKey(0)