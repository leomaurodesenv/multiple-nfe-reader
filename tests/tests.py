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
from nfeReader import barcode, qrcode, ocr


#--------------------------------------------
#-- Testing
#--------------------------------------------
def showImage(imageArray, imageName="Without name"):
    cv2.imshow('Image - %s' % imageName,imageArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def checkAllImages(imagesPath, decoder, display=False):
    for image in imagesPath:
        # decoding
        decoding, imgArray = decoder(image)
        for decodedItem in decoding:
            print("-[INFO] Found {} code: {}".format(decodedItem['type'], decodedItem['data']))
        # display
        if display:
            showImage(imgArray, image)


def checkOCRFromImages(imagesPath, decoder, display=False):
    for image in imagesPath:
        # decoding
        decoding = decoder(image)
        print("-[OCR] Found '{}':".format(image))
        print(decoding)
        # display
        if display:
            imgArray = cv2.imread(image,0)
            showImage(imgArray, image)


#--------------------------------------------
#-- Main
#--------------------------------------------
if __name__ == '__main__':
    # barcode
    print('\n-- Testing: barcode')
    checkAllImages(datasets.barcodeImages, barcode.decode, display=True)
    # QR code
    print('\n-- Testing: qrcode')
    checkAllImages(datasets.qrcodeImages, qrcode.decode, display=True)
    # OCR
    print('\n-- Testing: OCR - Optical Character Recognition')
    checkOCRFromImages(datasets.ocrImages, ocr.decode, display=True)