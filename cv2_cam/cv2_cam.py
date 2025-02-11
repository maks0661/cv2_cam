import cv2

# обученный классификатора для распознавания лица
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# видеопоток с вебки
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("не работает")
    exit()

while True:
    # захват кадра
    ret, frame = cap.read()
    if not ret:
        print("плохой кадр")
        break

    # кадр в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # лицо в кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # прямоугольник вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # кадр в данный момент
    cv2.imshow('rabotaet', frame)

    # кнопка = выход
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
