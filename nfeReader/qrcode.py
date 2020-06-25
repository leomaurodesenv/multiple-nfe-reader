#--------------------------------------------
#-- Libraries
#--------------------------------------------
import cv2
import numpy as np
from pyzbar.pyzbar import decode as qrDecode


#--------------------------------------------
#-- Modules
#--------------------------------------------
def decodeFromArray(imageArray):
    '''
    @module: nfeReader::qrcode::decodeFromArray
    Decode QR code from a image array
    @param imageArray: numpy.array
    @return: decoded code, image array
    @access: public
    '''
    # loading image, in GRAY scale
    decoding = qrDecode(imageArray)
    # return
    decodeImages = [{'data': dec.data, 'type': dec.type} for dec in decoding]
    return decodeImages, imageArray


def decodeFromFile(imagePath):
    '''
    @module: nfeReader::qrcode::decodeFromFile
    Decode QR code from a image file
    @param imagePath: image path
    @return: decoded code, image array
    @access: public
    '''
    # loading image, in GRAY scale
    imageArray = cv2.imread(imagePath,0)
    # return
    return decodeFromArray(imageArray)


def decode(image):
    '''
    @module: nfeReader::qrcode::decode
    Decode QR code from a image file or image array
    @param image: image path or image array
    @return: decoded code, image array
    @access: public
    '''
    # is image or array?
    return decodeFromArray(image) if isinstance(image, np.ndarray) \
        else decodeFromFile(image)