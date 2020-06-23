#--------------------------------------------
#-- Libraries
#--------------------------------------------
import cv2
from pyzbar.pyzbar import decode as qrDecode


#--------------------------------------------
#-- Modules
#--------------------------------------------
def decode(imagePath):
    '''
    @module: nfeReader::qrcode::decode
    Decode QR code from a image
    @param imagePath: image path
    @return: decoded code, image array 
    @access: public
    '''
    # loading image, in GRAY scale
    imageArray = cv2.imread(imagePath,0)
    decoding = qrDecode(imageArray)
    # return
    decodeImages = [{'data': dec.data, 'type': dec.type} for dec in decoding]
    return decodeImages, imageArray
