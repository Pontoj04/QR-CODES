import qrcode

# Your link
url = "https://www.youtube.com/watch?v=LKUkcHz3iu0"

# Generate QR code
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill="black", back_color="white")

# Define the path
save_path = r"C:\Users\PONTOJ04\OneDrive - Pfizer\Escritorio\qrcode.png"

# Save the QR code to the specified location
img.save(save_path)

print(f"QR Code saved at: {save_path}")
