import cv2

img = cv2.imread("resim.jpg") # resim dosyasını okur ve img değişkenine atar

blurred = cv2.GaussianBlur(img, (7, 7), 0) # 7x7'lik bir çekirdek kullanarak yumuşat

cv2.imshow("Bulank", blurred)

cv2.waitKey(0)
