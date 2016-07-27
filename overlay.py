from PIL import Image


def overlay(original_image_path):
    background = Image.open(original_image_path)
    overlay = Image.open('overlay.png')

    background = background.convert('RGBA')
    overlay = overlay.convert('RGBA')

    background = background.resize(overlay.size);

    new_img = background
    new_img.paste(overlay, (0, 0), overlay)
    new_img.save(original_image_path,'PNG')
