from PIL import Image, ImageOps
import os
import uuid

def convert_to_jpg(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpeg', '.gif', '.bmp', 'avif', '.jpg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, str(uuid.uuid4()) + '.png')
            try:
                with Image.open(input_path) as img:
                    img = ImageOps.fit(img, (512,512))
                    img.convert('RGB').save(output_path)
            except Exception as e:
                print(f"Error '{filename}': {e}")

input_folder = "./src/storage/test/1"
output_folder = "./src/storage/test"

convert_to_jpg(input_folder, output_folder)
