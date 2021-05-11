# Import QRCode from pyqrcode
import pyqrcode
import png

# String which represents the QR code
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Variable conatining link
url = "https://www.youtube.com/watch?v=choF2JRgjHY"

# Generating QR code
qrcode = pyqrcode.create(url)

# Create and save the png file naming "myqr.png"
qrcode.png('MustScan.png', scale = 6)

# Create and save the png file
qrcode.png('QRCODE.png', scale = 6)

