import cv2
import numpy

try:
    while True:
        image = cv2.imread('mall.png')

        cv2.imshow('mall', image)

        if cv2.waitKey(100) == 0x1b:
            print('ESC pressed. Exiting ...')
            break

except (KeyboardInterrupt, SystemExit):
    print('CTRL-C pressed. Exiting ...')
    sys,exit(0)
finally:
    cv2.destroyAllWindows()
