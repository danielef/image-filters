import argparse
import cv2
import numpy as np

def __show(imgs, show, title='image'):
    matrix = np.concatenate(imgs, axis=1)
    if show:
        cv2.imshow(title, matrix)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

def read_image(path, show=True):
    ans = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    return ans

def blur(img):
    ans = cv2.blur(img, (3, 3))
    return ans

def grey(img):
    chan2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    chan3 = cv2.cvtColor(chan2, cv2.COLOR_GRAY2BGR)
    return (chan2, chan3)

def sobel(img):
    ans = cv2.Sobel(img, cv2.CV_8U, 1, 0, 3, 1, borderType=cv2.BORDER_DEFAULT)
    return ans

def threshold(img):
    ans = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY_INV)
    return ans

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visual', action='store_true', help='open graphical view of processed images')
    parser.add_argument('-p', '--path', help='image to filter')
    args = parser.parse_args()
    
    if args.path is None:
        parser.print_help()
        exit(1)

    original = read_image(args.path, args.visual)
    grey2, grey3 = grey(original)
    blur = blur(grey2)
    sobel = sobel(blur)
    _, _threshold= threshold(sobel)
    _, t2 = threshold(grey2)

    print('blur: {}'.format(blur))
    print('sobel: {}'.format(sobel))
    print('threshold: {}'.format(_threshold))

    __show((grey2, blur, sobel, _threshold, t2), True)
    
    
