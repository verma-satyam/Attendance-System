import cv2
import os

mypath = 'ImagesAttendance'
myList = os.listdir(mypath)

def newPerson():
    name = str(input('Enter Name:'))
    rno = str(input('Enter Roll Number'))
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to grab Picture")
            break
        cv2.imshow('Webcam',img)
        k = cv2.waitKey(1)
        if k%256 == 27:
            #ESC pressed
            print('Escape Pressed, Closing!')
            break
        elif k%256 == 32:
            #SPACE PRESSED
            img_name = f'{name}-{rno}.jpg'
            cv2.imwrite(f'{mypath}/{img_name}',img)
            print(f'{img_name} Saved!')
            print('Details Saved!')
            break
    cap.release()
    cv2.destroyAllWindows()

