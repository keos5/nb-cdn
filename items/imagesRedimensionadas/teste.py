import os
from PIL import Image

input_folder = os.getcwd()
output_folder = os.path.join(input_folder, "imagesRedimensionadas")

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".png"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        with Image.open(input_path) as img:
            # força RGBA para preservar transparência corretamente
            img = img.convert("RGBA")
            width, height = img.size

            # Se for quadrada, vira 100x100
            if width == height:
                resized = img.resize((100, 100), Image.LANCZOS)
                resized.save(output_path, format="PNG")
                print(f"{file} -> 100x100")

            # Se alguma dimensão passar de 200, reduz proporcionalmente
            elif width > 200 or height > 200:
                ratio = min(200 / width, 200 / height)
                new_width = int(width * ratio)
                new_height = int(height * ratio)

                resized = img.resize((new_width, new_height), Image.LANCZOS)
                resized.save(output_path, format="PNG")
                print(f"{file} -> {new_width}x{new_height}")

            # Se não precisar redimensionar, só salva igual
            else:
                img.save(output_path, format="PNG")
                print(f"{file} -> mantida")
