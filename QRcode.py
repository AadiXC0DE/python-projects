import qrcode
import cv2
#pip install cv2 and qrcode 
def generate_qr_code(data, filename, error_correction, box_size, border):
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(filename)

def scan_qr_code(image_filename):
    image = cv2.imread(image_filename)
    detector = cv2.QRCodeDetector()
    retval, decoded_info, points, _ = detector.detectAndDecode(image)

    if retval:
        print("Decoded QR Code:")
        print(decoded_info)
    else:
        print("No QR code found or decoding failed.")

def main():
    while True:
        print("\nQR Code Generator and Scanner")
        print("1. Generate QR Code")
        print("2. Scan QR Code")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter the data for the QR code: ")
            filename = input("Enter the filename for the QR code image (e.g., qr_code.png): ")
            error_correction = input("Enter error correction level (L, M, Q, H): ").upper()
            box_size = int(input("Enter box size: "))
            border = int(input("Enter border size: "))
            generate_qr_code(data, filename, error_correction, box_size, border)
            print(f"QR code generated and saved as {filename}.")
        elif choice == '2':
            image_filename = input("Enter the filename of the QR code image to scan: ")
            scan_qr_code(image_filename)
        elif choice == '3':
            print("Exiting QR Code Generator and Scanner.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
