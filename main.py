import serial
import cv2
from cvzone.ClassificationModule import Classifier
import time

serialobj=serial.Serial('COM6')
cap = cv2.VideoCapture(1)  # Initialize video capture
    # path = "C:/Users/USER/Documents/maskModel/"
maskClassifier = Classifier('C:\\Users\\Asus\Desktop\\Waste_Classifier\\Model\\keras_model.h5', 'C:\\Users\\Asus\Desktop\\Waste_Classifier\\Model\\labels.txt')

custom_threshold = 0.95  

while True:
    # Read frame from camera
    
    _, img = cap.read()
    if img is None:
        print("Error: Couldn't read frame.")
        break


    prediction = maskClassifier.getPrediction(img)
    print(prediction[1])

    # Act based on prediction
    if prediction[0][prediction[1]] >= custom_threshold:
        if prediction[1] == 0:
            print("Plastic")
            serialobj.write(b'A')
            time.sleep(10)
        elif prediction[1] == 1:
            print("Metal")
            serialobj.write(b'B')
            time.sleep(10)
        elif prediction[1] == 2:
            print("Battery")
            serialobj.write(b'C')
            time.sleep(10)
    else:
        print("Nothing")

    # Show image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Break the loop if 'q' is pressed
    time.sleep(2)

# Release resources
cap.release()
cv2.destroyAllWindows()
serialobj.close()