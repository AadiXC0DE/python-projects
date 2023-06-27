import qrcode
#pip install qrcode first

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(filename)

data = "Hello, world!"
filename = "qr_code.png"
generate_qr_code(data, filename)
print(f"QR code generated and saved as {filename}.")
