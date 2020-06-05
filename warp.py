import argparse
import cv2
import numpy as np
import sys
import time

# Image transformation script


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', required=True, help='Input directory to take images')
    parser.add_argument('-c', '--config', required=False, help='YAML points file'

    args = parser.parse_args()

    video = args.video
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

        # Transformation matrix
        M = cv2.getPerspectiveTransform(np.array(points, dtype=np.float32),
                                        np.array(dest, dtype=np.float32))

        # Reference point in source coordinates
        ref = (605, 73)

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

            cv2.circle(image_resized, ref, 5, (0, 165, 255), -1)

            for i in range(0, len(points)):
                j = i + 1 if i + 1 < len(points) else 0
                cv2.line(image_resized,points[i], points[j], (255, 0, 0), 1)

            now = time.time()

            # Create a new image applying Transformation Matrix
            dst = cv2.warpPerspective(image_resized, M, (600, 900))

            # Reference point proyection in new plane
            new_ref = cv2.perspectiveTransform(np.array([[ref]],  dtype='float64'), M)
            cv2.circle(dst, (int(new_ref[0][0][0]), int(new_ref[0][0][1])), 5, (0, 255, 0), -1)

            print("delta: {}".format((time.time() - now) * 1000))

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
