import qrcode
import os

def generate_qr_code(data, output_folder, filename):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each "box" of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    output_path = os.path.join(output_folder, filename)
    img.save(output_path)
    print(f"QR code saved to {output_path}")

# Example usage
text_or_url = "text or url"
output_folder = os.path.join(os.path.join(os.environ['USERPROFILE'], 'Desktop'), "QR Codes")
filename = "example_qr_code.png"

generate_qr_code(text_or_url, output_folder, filename)
