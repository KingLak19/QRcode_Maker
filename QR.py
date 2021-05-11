# Import QRCode from pyqrcode
import pyqrcode
import png

# String which represents the QR code
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Generate QR code
qrcode = pyqrcode.create(url)

# Create and save the png file naming "myqr.png"
qrcode.png('MustScan.png', scale = 6)
