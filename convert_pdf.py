from PIL import Image

# Open the image file
image_path = 'receipt-image.jpg'
image = Image.open(image_path)

# Convert the image to PDF
pdf_path = 'receipt-nonsearchable.pdf'
image.save(pdf_path, 'PDF', resolution=100.0)

print(f"Image successfully converted to {pdf_path}")
