import cv2 as cv
import pyautogui
from PIL import Image
import serial
import time
import colorsys
arduino=serial.Serial('COM5', 960000)
time.sleep(2)

def hsv2rgb(h,s,v):
        return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h/360,s/100,v/100))

def rgb_to_hsv(r, g, b):
 
    # R, G, B values are divided by 255
    # to change the range from 0..255 to 0..1:
    r, g, b = r / 255.0, g / 255.0, b / 255.0
 
    # h, s, v = hue, saturation, value
    cmax = max(r, g, b)    # maximum of r, g, b
    cmin = min(r, g, b)    # minimum of r, g, b
    diff = cmax-cmin       # diff of cmax and cmin.
 
    # if cmax and cmax are equal then h = 0
    if cmax == cmin:
        h = 0
     
    # if cmax equal r then compute h
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
 
    # if cmax equal g then compute h
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
 
    # if cmax equal b then compute h
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
 
    # if cmax equal zero
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
 
    # compute v
    v = cmax * 100
    return h, s, v

G = 1
while G == 1:
    time.sleep(.01)
    start = time.time()
    SS = pyautogui.screenshot()
    SS = SS.resize((3,3))
##    SS = SS.convert('HSV')pil
    SS = SS.getpixel((2,2))
##    red = SS[0]
##    green = SS[1]
##    blue = SS[2]
    r = int(SS[0])
    g = int(SS[1])
    b = int(SS[2])
    SS = rgb_to_hsv(r,g,b)
    H = int(SS[0])
    S = int(SS[1] *2)
    V = int(SS[2])
    if S > 100:
        S = 100
    SS = hsv2rgb(H, S, V)
    r = int(SS[0])
    g = int(SS[1])
    b = int(SS[2])
    r = int(r)
    g = int(g)
    b = int(b)
    r = str(r)
    g = str(g)
    b = str(b)
    print(r)
    print(g)
    print(b)
    if len(r) == 1:
        try:
            arduino.write(b'0')
            arduino.write(b'0')
            redc = str(r[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass    
    if len(r) == 2:
        try:
            arduino.write(b'0')
            redc = str(r[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(r[1])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
    if len(r) == 3:
        try:
            redc = str(r[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(r[1])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(r[2])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
##    print(len(g))
##    print(g)
    arduino.write(b'x')
    if len(g) == 1:
        try:
            arduino.write(b'0')
            arduino.write(b'0')
            redc = str(g[0])
            red = redc.encode()
            arduino.write(red)
            print("mmhmmm")
        except Exception:
            print("error")
            pass    
    if len(g) == 2:
        try:
            arduino.write(b'0')
            redc = str(g[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(g[1])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
    if len(g) == 3:
        try:
            redc = str(g[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(g[1])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(g[2])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
    arduino.write(b'x')
    if len(b) == 1:
        try:
            arduino.write(b'0')
            arduino.write(b'0')
            redc = str(b[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass    
    if len(b) == 2:
        try:
            arduino.write(b'0')
            redc = str(b[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(b[1])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
    if len(b) == 3:
        try:
            redc = str(b[0])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(b[1])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
        try:
            redc = str(b[2])
            red = redc.encode()
            arduino.write(red)
        except Exception:
            print("error")
            pass
    arduino.write(b'x')
    end = time.time()
    print(str(end - start) + "sec")
##    time.sleep(1)

