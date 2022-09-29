import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR Code
s = "https://bit.ly/3LP9wm6"

# Generate QR Code
url = pyqrcode.create(s)

# Create and save the SVG file and giving it a name
url.svg("sickQR.svg", scale=8)

# Create and save the PNG file and giving it a name
url.png("sickQR.png", scale=6)
