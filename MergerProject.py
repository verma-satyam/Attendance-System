import AttendanceProject
import test
import SavePerson

while True:
    choice = int(input('Enter 1 to detect Face Mask and 2 to Mark Attendance:'))
    if choice == 1:
        test.detectMask()
    elif choice == 2:
        AttendanceProject.detectFace()
    elif choice == 0:
        break
    elif choice == 3:
        print('Enter Name and Roll Number of New Person')
        SavePerson.newPerson()


