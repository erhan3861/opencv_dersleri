import cv2
import numpy as np

# 1. Kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    # 2. Kameradan anlık kare oku
    ret, frame = cap.read()
    if not ret:
        break

    # 3. Görüntüyü BGR'den HSV formatına çevir
    # Neden? Çünkü HSV'de renk (Hue) tek bir kanaldır, ışık değişiminden az etkilenir.
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 4. Tespit etmek istediğimiz rengin alt ve üst sınırlarını belirle (Mavi için)
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # 5. Maskeleme yap: Belirlen aralıktaki pikseller BEYAZ, diğerleri SİYAH olsun
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # 6. Sonuçları ekranda göster
    cv2.imshow("Kamera Goruntusu", frame) # Normal hali
    cv2.imshow("Mavi Objeleri Takip Et", mask) # Sadece mavilerin göründüğü maske

    # 'q' tuşuna basınca döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()