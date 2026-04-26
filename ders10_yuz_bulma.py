# link: https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

import cv2

# Hazır yüz tanıma dosyasını yükle

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')# Yüzleri bul

img = cv2.imread("milli_takim.webp") # resim dosyasını okur ve img değişkenine atar

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Yüz tanıma için gri formata dönüştür

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)# Yüzlerin etrafına kutu çizfor (x, y, w, h) in faces:

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)


cv2.imshow("Yüzler", img)

cv2.waitKey(0)
