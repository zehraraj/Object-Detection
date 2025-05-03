
import serial
# import codebug_tether
import time
from PIL import Image
import io
import base64
# import rawpy
import imageio
import cv2


arduino = serial.Serial(port='/dev/cu.Bluetooth-Incoming-Port', baudrate=250000, timeout=.1)

def write_read():
##    arduino.write(bytes(x, 'utf-8'))
##    time.sleep(1)
    data = arduino.read_until().strip().decode()
    if(len(data) > 0):
        cv2.destroyAllWindows()
        print(int(data)) # printing the value
        time.sleep(1)
        imgdata = arduino.read(int(data))
        print(type(imgdata))
            
        image_result = open('deer_decode.jpeg', 'wb') # create a writable image and write the decoding result
        image_result.write(imgdata)
        image_result.close()
        print("image saved")
        
        img = cv2.imread('deer_decode.jpeg')
        cv2.imshow('image',img)
        cv2.waitKey(1)
        
while True:
    #num = input("Enter a number: ") # Taking input from user
    try:
        value = write_read()
    except:
        pass
