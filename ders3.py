import cv2

img = cv2.imread("resim.jpg") # resim dosyasını okur ve img değişkenine atar

# Dikdörtgen çizimi: (resim, sol_ust, sag_alt, renk, kalinlik)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

cv2.circle(img, (300, 300), 50, (0, 0, 255), -1) # Daire çizimi: (resim, merkez, yaricap, renk, kalinlik)

cv2.putText(img, "Muhendislik", (60, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Cizim", img)

cv2.waitKey(0)