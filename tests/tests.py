#--------------------------------------------
#-- Libraries
#--------------------------------------------
# system imports
import os
import sys

# add parent path to python paths
parentdir = os.path.join(os.path.dirname(__file__), '../')
sys.path.insert(0,parentdir) 

# imports
import cv2
import datasets
from nfeReader import barcode, qrcode


#--------------------------------------------
#-- Testing
#--------------------------------------------
def showImage(imageArray, imageName):
    cv2.imshow('Image - %s' % imageName,imageArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def checkAllImages(imagesPath, decoder, display=False):
    for image in imagesPath:
        # decoding
        decoding, imgArray = decoder(image)
        for decodedItem in decoding:
            print("[INFO] Found {} code: {}".format(decodedItem['type'], decodedItem['data']))
        # display
        if display:
            showImage(imgArray, image)


#--------------------------------------------
#-- Main
#--------------------------------------------
if __name__ == '__main__':
    print('-- Testing: barcode')
    checkAllImages(datasets.barcodeImages, barcode.decode, display=True)
    print('-- Testing: qrcode')
    checkAllImages(datasets.qrcodeImages, qrcode.decode, display=True)