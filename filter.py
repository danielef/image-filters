import argparse
import cv2
import numpy as np

def __show(imgs, show, title='image'):
    matrix = np.concatenate(imgs, axis=1)
    matrix2 = np.concatenate(imgs, axis=1)
    print(matrix)
    m2 = np.concatenate((matrix, matrix2))
    print('concatenate2:')
    print(m2)
    if show:
        cv2.imshow(title, m2)
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

def decolor(img):
    gray = np.zeros(img.shape, np.uint8)
    gray = cv2.cvtColor(gray, cv2.CV_8UC1)
    color_boost = np.zeros(img.shape, np.uint8)
    color_boost = cv2.cvtColor(color_boost, cv2.CV_8UC3)
    decolor = cv2.decolor(img, gray, color_boost)
    return decolor
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--visual', action='store_true', help='open graphical view of processed images')
    parser.add_argument('-p', '--path', help='image to filter')
    
    args = parser.parse_args()
    
    if args.path is None:
        parser.print_help()
        exit(1)
        
    original = read_image(args.path, args.visual)
    
    # Using default cvtColor to grey
    #grey_2chan, grey_3chan = grey(original)
    #grey2blur = blur(grey_2chan)
    #grey2sobel = sobel(grey2blur)
    #_, grey2threshold = threshold(grey2sobel)
    
    # decolor
    grayscale, color_boost = decolor(original)
    
    # Using grayscale
    #gs2blur = blur(grayscale)
    #gs2sobel = sobel(gs2blur)
    #_, gs2threshold = threshold(gs2sobel)

    # Double decolor
    #color_boost2, _ = decolor(color_boost)
    #cb2blur = blur(color_boost2)
    #cb2sobel = sobel(cb2blur)
    #_, cb2threshold = threshold(cb2sobel)

    #normal = np.concatenate((grey_2chan, grey2blur, grey2sobel, grey2threshold), axis=1)
    #decolors = np.concatenate((grayscale, gs2blur, gs2sobel, gs2threshold), axis=1)
    #decolorx2 = np.concatenate((color_boost2, cb2blur, cb2sobel, cb2threshold), axis=1)
            
    cv2.imwrite('decolor-{}'.format(args.path), grayscale)
    cv2.imwrite('color_boost-{}'.format(args.path), color_boost)

    cv2.waitKey(0) 
    cv2.destroyAllWindows()
    
    
    
