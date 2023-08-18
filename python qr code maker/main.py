import qrcode

# Allows user to enter text or link to convert to a QR code
link = input("Enter text or link: ")

# Create a QR code instance
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data to the QR code instance
qr.add_data(link)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image as a PNG file
img.save("qrcode.png")
