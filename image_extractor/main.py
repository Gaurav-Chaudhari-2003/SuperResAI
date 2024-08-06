import os
from pdf2image import convert_from_path
from PIL import Image


def pdf_to_images(pdf_path, output_folder):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save images to the output folder
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, "PNG")
        print(f"Saved {image_path}")


# Path to the PDF file
pdf_path = 'C:\\Users\\chaud\\Downloads\\temp\\tempHe.pdf'
# Output folder for PNG images
output_folder = 'output_images'

pdf_to_images(pdf_path, output_folder)
