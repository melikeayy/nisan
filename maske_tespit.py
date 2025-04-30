import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # Yüz tespiti için
mouth_cascade = cv2.CascadeClassifier("haarcascade_mcs_mouth.xml") # Ağız tespiti


cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kameradan görüntü alınamıyor.")
            break

        frame = cv2.resize(frame, (640, 480))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Griye dönüştürme
        gray = cv2.equalizeHist(gray)  # Işık koşullarını iyileştirme

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            
            # Yüzün alt yarısında ağız arama
            roi_gray = gray[y+int(h*0.6):y+h, x:x+w]
            mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=15, minSize=(25, 15))

            if len(mouths) > 0:
                cv2.putText(frame, "MASKE YOK!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            else:
                cv2.putText(frame, "MASKE VAR", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("Maske Kontrol", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()