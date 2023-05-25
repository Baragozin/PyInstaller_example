import time
from PIL import Image

# Ask the user for the input image file
input_file = input('Input 42.jpg')

# Open the input image file using Pillow
with Image.open(input_file) as img:
    # Rotate the image by 90 degrees
    img_rotated = img.rotate(90)

    # Convert the image to grayscale
    img_grayscale = img.convert('L')

    # Resize the image to half its original size
    img_resized = img.resize((img.width//2, img.height//2))

    # Save the manipulated image data to a file
    img_rotated.save('output_rotated.png')
    img_grayscale.save('output_grayscale.png')
    img_resized.save('output_resized.png')

print("Check your folder.")
time.sleep(2)
input("Нажмите Enter для выхода")