# Import QRCode from pyqrcode
import pyqrcode
import png

# Variable conatining link
url = "https://www.youtube.com/watch?v=choF2JRgjHY"

# Generating QR code
qrcode = pyqrcode.create(url)

# Create and save the png file
qrcode.png('QRCODE.png', scale = 6)
