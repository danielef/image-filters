import cv2
import numpy as np
import sys

try:
    while True:
        image = cv2.imread('mall.png')
        image_resized = cv2.resize(image, (1280, 720))
        cv2.circle(image_resized, 

        cv2.imshow('mall', image_resized)
        
        

        if cv2.waitKey(100) == 0x1b:
            print('ESC pressed. Exiting ...')
            break

except (KeyboardInterrupt, SystemExit):
    print('CTRL-C pressed. Exiting ...')
    sys,exit(0)
finally:
    cv2.destroyAllWindows()
