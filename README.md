# nfeReader package [in construction]
   
Read multiples details from a "NFe - Nota Fiscal eletrônica".   
-   This package uses [pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) and [opencv](https://github.com/skvark/opencv-python).
-   [Nota Fiscal eletrônica (PT-BR)](https://bomcontrole.com.br/cupom-fiscal-eletronico-sat/) details
-   Barcode and QR code
    -   [Generators](https://barcode.tec-it.com/en/Code128)
    -   [Symbologies](https://www.tec-it.com/en/support/knowbase/barcode-overview/linear/Default.aspx)

---
## Package

This package can:
1.  Decode barcode from images.
2.  Decode QR code from images.
3.  Read text from images _(working on)_.

---
## Installation

Install the requirements to use this package.

```shell
#-- installing the requirements
$ pip install -r requirements.txt
```

Or install this package in your environment.   

```shell
#-- installing the package
$ python -m pip install --user --upgrade setuptools wheel
$ python setup.py install
```

---
## Coding

Suprise yourself viewing [tests/tests.py](tests/tests.py).   
```python
from nfeReader import barcode, qrcode

barcode.decode('image/path')
qrcode.decode('image/path')
```

---
## Also look ~

-   [License MIT](LICENSE)
-   Create by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)
