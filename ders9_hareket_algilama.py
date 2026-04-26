import cv2

# 1. Kamerayı başlat
cap = cv2.VideoCapture(0)

# İlk kareyi oku (karşılaştırma yapmak için bir başlangıç lazım)
ret, kare1 = cap.read()
gray1 = cv2.cvtColor(kare1, cv2.COLOR_BGR2GRAY)

while True:
    # 2. Yeni kareyi oku
    ret, kare2 = cap.read()
    gray2 = cv2.cvtColor(kare2, cv2.COLOR_BGR2GRAY)

    # 3. İki kare arasındaki mutlak farkı bul
    # (Matematiksel çıkarma: |kare1 - kare2|)
    fark = cv2.absdiff(gray1, gray2)

    # 4. Farkı ekranda göster
    cv2.imshow("Hareket Analizi", fark)

    # 5. Bir sonraki adım için kareyi güncelle
    gray1 = gray2

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()