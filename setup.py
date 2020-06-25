import setuptools

with open('requirements.txt', 'r') as f:
    reqs = f.read().splitlines()

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='nfeReader',
    version='0.0.3',
    author='Leonardo Mauro',
    author_email='leo.mauro.desenv@gmail.com',
    description='Multiple  NFe reader - barcode, QR code, and OCR reader',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/leomaurodesenv/mutiple-nfe-reader',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=reqs
)