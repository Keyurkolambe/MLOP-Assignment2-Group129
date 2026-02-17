from PIL import Image
from src.preprocess_utils import resize_rgb_image

def test_resize_rgb_image():
    img = Image.new("L", (500, 300))  # grayscale dummy
    out = resize_rgb_image(img, (224, 224))

    assert out.mode == "RGB"
    assert out.size == (224, 224)
