import cv2
import numpy as np
import sys

try:
    while True:
        image = cv2.imread('mall.png')
        image_resized = cv2.resize(image, (1280, 720))
        points = [(15, 696),
                  (349, 18),
                  (908, 12),
                  (1265, 674)]
        cv2.circle(image_resized, points[0], 5, (0, 255, 255), -1)
        cv2.circle(image_resized, points[1], 5, (255, 0, 255), -1)
        cv2.circle(image_resized, points[2], 5, (255, 255, 0), -1)
        cv2.circle(image_resized, points[3], 5, (0, 0, 255), -1)

        for i in range(0, len(points)):
            j = i + 1 if i + 1 < len(points) else 0
            cv2.line(image_resized,points[i], points[j], (255, 0, 0), 1)

        cv2.imshow('mall', image_resized)
        
        

        if cv2.waitKey(100) == 0x1b:
            print('ESC pressed. Exiting ...')
            break

except (KeyboardInterrupt, SystemExit):
    print('CTRL-C pressed. Exiting ...')
    sys,exit(0)
finally:
    cv2.destroyAllWindows()
