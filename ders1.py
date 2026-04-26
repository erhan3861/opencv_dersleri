# pip install opencv-python

import cv2 # OpenCV kütüphanesini içe aktarır

img = cv2.imread("resim.jpg") # resim dosyasını okur ve img değişkenine atar

cv2.imshow("Ilk Goruntu", img) # resimi ekranda gösterir

cv2.waitKey(0) # Bir tuşa basana kadar bekler

cv2.destroyAllWindows() # Tüm OpenCV pencerelerini kapatır