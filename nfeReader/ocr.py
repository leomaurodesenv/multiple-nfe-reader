#--------------------------------------------
#-- Libraries
#--------------------------------------------
import pytesseract as decoder
from PIL import Image
import numpy as np

# predefinitions
default_language = 'por'


#--------------------------------------------
#-- Modules
#--------------------------------------------
def decodeFromArray(imageArray):
    '''
    @module: nfeReader::ocr::decodeFromArray
    Decode characters from a image array
    @param imageArray: numpy.array
    @return: decoded message
    @access: public
    '''
    image = Image.fromarray(imageArray)
    phrase = decoder.image_to_string(image, lang=default_language)
    return phrase


def decodeFromFile(imagePath):
    '''
    @module: nfeReader::ocr::decodeFromFile
    Decode characters from a image file
    @param imagePath: image path
    @return: decoded message
    @access: public
    '''
    image = Image.open(imagePath)
    phrase = decoder.image_to_string(image, lang=default_language)
    return phrase


def decode(image):
    '''
    @module: nfeReader::ocr::decode
    Decode characters from a image file or image array
    @param image: image path or image array
    @return: decoded message
    @access: public
    '''
    # is image or array?
    return decodeFromArray(image) if isinstance(image, np.ndarray) \
        else decodeFromFile(image)
