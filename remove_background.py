from rembg import remove
from PIL import Image
import io

def remove_background(input_image_path, output_image_path):
    with open(input_image_path, 'rb') as input_image_file:
        input_data = input_image_file.read()

    output_image_data = remove(input_data)

    with open(output_image_path, 'wb') as output_image_file:
        output_image_file.write(output_image_data)
    
    print("Background removed for the input image")

input_image = '3.jpeg'
output_image = '3.jpeg'

remove_background(input_image, output_image)