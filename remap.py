import argparse
import cv2
import numpy as np
import sys
import time

# Image transformation script


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', required=True, help='Input directory to take images')
    parser.add_argument('-c', '--config', required=False, help='YAML points file')

    args = parser.parse_args()

    video = args.video
    try:
        # Video Capturre
        cap = cv2.VideoCapture(video)

        k1 = -0.00010999999999999999
        k2 = 0.0
        p1 = 0.00035000000000000027
        p2 = -0.002230000000000005
        k3 = 0.0

        fx = -49.0
        cx = 101.0
        fy = -49.0
        cy = 101.0

        while True:
            success, image  = cap.read()

            K  = np.array([[fx, 0.0, cx],
                           [0.0, fy, cy],
                           [0.0, 0.0, 1.0]])
            
            d =  np.array([k1, k2, p1, p2, k3])

            if success == False :
                print('Trying to reconnect ...')
                cap = cv2.VideoCapture(video) 
                continue

            h, w = image.shape[:2]
            image_resized = cv2.resize(image, (1280, 720))

            now = time.time()            

            newcameramatrix, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0)

            mapx, mapy = cv2.initUndistortRectifyMap(K, d, None, newcameramatrix, (w, h), 5)

            dst = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

            print("delta: {}, k1: {}, k2: {}, p1: {}, p2: {}, k3: {}, fx: {}, cx: {}, fy: {}, cy: {}".format((time.time() - now) * 1000, k1, k2, p1, p2, k3, fx, cx, fy, cy))

            cv2.imshow('mall', image)
            cv2.imshow('dest', dst)

            key = cv2.waitKey(100)

            if key == 0x1b:
                print('ESC pressed. Exiting ...')
                break
            elif key & 0xff == ord('q'):
                k1 = k1 + 0.00001
            elif key & 0xff == ord('a'):
                k1 = k1 - 0.00001
            elif key & 0xff == ord('w'):
                k2 = k2 + 0.00001
            elif key & 0xff == ord('s'):
                k2 = k2 - 0.00001
            elif key & 0xff == ord('e'):
                p1 = p1 + 0.00001
            elif key & 0xff == ord('d'):
                p1 = p1 - 0.00001
            elif key & 0xff == ord('r'):
                p2 = p2 + 0.00001
            elif key & 0xff == ord('f'):
                p2 = p2 - 0.00001
            elif key & 0xff == ord('t'):
                k3 = k3 + 0.00001
            elif key & 0xff == ord('g'):
                k3 = k3 - 0.00001

            elif key & 0xff == ord('p'):
                fx = fx + 50.0000
                fy = fy + 50.0000
            elif key & 0xff == ord('l'):
                fx = fx - 50.0000
                fy = fy - 50.0000
            elif key & 0xff == ord('o'):
                cx = cx + 50.0000
                cy = cy + 50.0000
            elif key & 0xff == ord('k'):
                cx = cx - 50.0000
                cy = cy - 50.0000
#            elif key & 0xff == ord('i'):
           
#            elif key & 0xff == ord('j'):
 
#            elif key & 0xff == ord('u'):
                
#            elif key & 0xff == ord('h'):

            else:
                print('nothing')

    except (KeyboardInterrupt, SystemExit):
        print('CTRL-C pressed. Exiting ...')
        sys,exit(0)
    finally:
        cv2.destroyAllWindows()
