from PIL import Image

def resize_rgb_image(img: Image.Image, size=(224, 224)) -> Image.Image:
    return img.convert("RGB").resize(size)
