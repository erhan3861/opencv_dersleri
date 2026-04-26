import cv2


cap = cv2.VideoCapture(0) # 0, varsayılan kamera

while True:
    ret, frame = cap.read() # Kameradan bir kare oku
    cv2.imshow("Canli Video", frame) # Kameradan okunan kareyi ekranda göster
    if cv2.waitKey(1) & 0xFF == ord('q'): # 'q'ya basınca çık
        break

cap.release() # Kamera kaynağını serbest bırak
cv2.destroyAllWindows()