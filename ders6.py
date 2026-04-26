import cv2

img = cv2.imread("resim.jpg") # resim dosyasını okur ve img değişkenine atar

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

edges = cv2.Canny(gray_img, 100, 200) # Alt ve üst eşik değerleri

cv2.imshow("Kenarlar", edges)

cv2.waitKey(0)