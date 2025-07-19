from rembg import remove
from PIL import Image
import io

def remove_bg(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()

    output_data = remove(input_data)

    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)

    print(f"Background removed and saved to {output_path}")

input_image = 'venkata_subbaiah.png'
output_image = 'venkata_subbaiah_image.png'
remove_bg(input_image, output_image)