import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR Code
test = "https://bit.ly/3LP9wm6"

s = input()

fileName = input('File name: ')

# Generate QR Code
url = pyqrcode.create(s)

# Create and save the SVG file and giving it a name
url.svg(f"{fileName}.svg", scale=8)

# Create and save the PNG file and giving it a name
url.png(f"{fileName}.png", scale=6)
