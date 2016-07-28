import PIL
from PIL import Image


def overlay(original_image_path):
    baseheight = 1024 
    background = Image.open(original_image_path)
    hpercent = (baseheight / float(background.size[1]))
    wsize = int((float(background.size[0]) * float(hpercent)))
    background = background.resize((wsize, baseheight), PIL.Image.BILINEAR)

    overlay = Image.open('overlay.png')
    pkmn = Image.open('pokemon-go-images/150.png')

    background = background.convert('RGBA')
    overlay = overlay.convert('RGBA')
    pkmn= pkmn.convert('RGBA')

    overlay = overlay.resize(background.size, PIL.Image.BILINEAR);

    new_img = background
    new_img.paste(overlay, (0, 0), overlay)

    new_img.paste(pkmn, (background.size[0]/2, background.size[1]/2), pkmn)

    new_img.save(original_image_path,'PNG')
