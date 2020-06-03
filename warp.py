import cv2
import numpy as np
import sys
import time

video = './mall.mp4'
try:
    # Video Capturre
    cap = cv2.VideoCapture(video)
    
    # Source perspective points
    points = [(349, 18),
              (908, 12),
              (1265, 674),
              (15, 696)]

    # Destination rectangle
    dest = [(0, 0), (600, 0), (600, 900), (0, 900)]
    M = cv2.getPerspectiveTransform(np.array(points, dtype=np.float32),
                                    np.array(dest, dtype=np.float32))

    while True:
        success, image  = cap.read()

        if success == False :
            print('Trying to reconnect ...')
            cap = cv2.VideoCapture(video) 
            continue

        image_resized = cv2.resize(image, (1280, 720))
        
        
        cv2.circle(image_resized, points[0], 5, (0, 255, 255), -1)
        cv2.circle(image_resized, points[1], 5, (255, 0, 255), -1)
        cv2.circle(image_resized, points[2], 5, (255, 255, 0), -1)
        cv2.circle(image_resized, points[3], 5, (0, 0, 255), -1)

        for i in range(0, len(points)):
            j = i + 1 if i + 1 < len(points) else 0
            cv2.line(image_resized,points[i], points[j], (255, 0, 0), 1)

        now = time.time()
        
        
        dst = cv2.warpPerspective(image_resized, M, (600, 900))
        print("M.shape: {}, delta: {}".format(M.shape, (time.time() - now) * 1000))

        cv2.imshow('mall', image_resized)
        cv2.imshow('dest', dst)
        

        if cv2.waitKey(100) == 0x1b:
            print('ESC pressed. Exiting ...')
            break

except (KeyboardInterrupt, SystemExit):
    print('CTRL-C pressed. Exiting ...')
    sys,exit(0)
finally:
    cv2.destroyAllWindows()
