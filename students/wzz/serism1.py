import serial

ser=serial.Serial("COM1")
#ser.write("100,200,100\n".encode())

while True:
    a=input("please input your cmd here:")
    print(a)
    if a=='q':
        break
    ser.write(a.encode())

