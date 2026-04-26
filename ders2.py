import cv2

img = cv2.imread("resim.jpg") # resim dosyasını okur ve img değişkenine atar

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # resmi gri formata dönüştürür ve gray_img değişkenine atar

cv2.imshow("Gri Format", gray_img) # gri formatta resmi ekranda gösterir

cv2.waitKey(0) # Bir tuşa basana kadar bekler