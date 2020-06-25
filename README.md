# nfeReader (in construction)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/63503e41c3b047858be4c86445f5e286)](https://www.codacy.com/manual/leomaurodesenv/multiple-nfe-reader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leomaurodesenv/multiple-nfe-reader&amp;utm_campaign=Badge_Grade)
   
Read multiples details from a "NFe - Nota Fiscal eletrônica".   
-   This package uses 
    -   [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) - read barcode and QR code 
    -   [opencv](https://github.com/skvark/opencv-python) - read and process images   
    -   [tesseract](https://github.com/tesseract-ocr/tesseract/wiki) - Optical Character Recognition (OCR)   
-   [Nota Fiscal eletrônica (PT-BR)](https://bomcontrole.com.br/cupom-fiscal-eletronico-sat/) details 
-   Barcode and QR code
    -   [Generators](https://barcode.tec-it.com/en/Code128)
    -   [Symbologies](https://www.tec-it.com/en/support/knowbase/barcode-overview/linear/Default.aspx)

---
## Package

This package can:
1.  Decode barcode from images.
2.  Decode QR code from images.
3.  Read text from images.

---
## Installation

Install the requirements to use this package.   
You have to install [tesseract](https://github.com/tesseract-ocr/tesseract/wiki) in your computer.   

```shell
#-- installing the requirements
$ pip install -r requirements.txt
```

Or install this package in your environment.   

```shell
#-- installing the package
$ python setup.py install
```

---
## Coding

Suprise yourself running [tests/tests.py](tests/tests.py).   
```python
from nfeReader import barcode, qrcode, ocr

# Decode from image file
barcode.decodeFromFile('image/path')
qrcode.decodeFromFile('image/path')
ocr.decodeFromFile('image/path')

# Decode from image array
barcode.decodeFromArray('numpy.array')
qrcode.decodeFromArray('numpy.array')
ocr.decodeFromArray('image/path')

# Decode from image file or image array
barcode.decode('image/path' or 'numpy.array')
qrcode.decode('image/path' or 'numpy.array')
ocr.decode('image/path' or 'numpy.array')
```

---
## Also look ~

-   [License MIT](LICENSE)
-   Create by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)
