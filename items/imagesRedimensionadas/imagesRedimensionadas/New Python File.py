import os
from PIL import Image

# Qualidade do WEBP
QUALITY = 95

# Se quiser apagar o original após converter
DELETE_ORIGINAL = False

# Extensões suportadas
EXTENSIONS = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")

def has_transparency(img):
    """
    Verifica se a imagem tem transparência.
    """
    if img.mode in ("RGBA", "LA"):
        return True

    if img.mode == "P":
        transparency = img.info.get("transparency", None)
        return transparency is not None

    return False

def convert_to_webp(path):
    try:
        with Image.open(path) as img:
            transparent = has_transparency(img)

            # Preserva transparência quando existir
            if transparent:
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")

            new_path = os.path.splitext(path)[0] + ".webp"

            img.save(
                new_path,
                "WEBP",
                quality=QUALITY,
                method=6,          # melhor compressão/qualidade
                lossless=False     # pode trocar para True em assets com transparência
            )

        print(f"Convertido: {path} -> {new_path}")

        if DELETE_ORIGINAL:
            os.remove(path)

    except Exception as e:
        print(f"Erro em {path}: {e}")

def main():
    root_dir = os.getcwd()

    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(EXTENSIONS):
                full_path = os.path.join(root, file)
                convert_to_webp(full_path)

if __name__ == "__main__":
    main()