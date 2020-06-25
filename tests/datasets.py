#--------------------------------------------
#-- Import
#--------------------------------------------
import os


#--------------------------------------------
#-- Definitions
#--------------------------------------------
datasetFolder = 'dataset/'
datasetFolder = os.path.join(os.path.dirname(__file__), datasetFolder)
barcodeFolder = os.path.join(datasetFolder, 'barcode/')
qrcodeFolder = os.path.join(datasetFolder, 'qrcode/')
ocrFolder = os.path.join(datasetFolder, 'ocr/')


#--------------------------------------------
#-- Functions
#--------------------------------------------
def _getFiles(folderPath):
    '''
    @module: dataset::_getFiles
    Retrive a list of file name from a folder path
    @param folderPath: folder path
    @return: list of file name
    @access: private
    '''
    fileList = os.listdir(folderPath)
    return fileList


def _getFilePath(folderPath):
    '''
    @module: dataset::_getFilePath
    Retrive a list of file path from a folder path
    @param folderPath: folder path
    @return: list of file path
    @access: private
    '''
    fileListPath = []
    fileList = _getFiles(folderPath)
    for fileName in fileList:
        filePath = os.path.join(folderPath, fileName)
        fileListPath.append(filePath)
    return fileListPath


#--------------------------------------------
#-- Images path
#--------------------------------------------
emptyImage = os.path.join(datasetFolder, 'empty.png')
barcodeImages = _getFilePath(barcodeFolder)
qrcodeImages = _getFilePath(qrcodeFolder)
ocrImages = _getFilePath(ocrFolder)
