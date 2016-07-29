import PIL
from PIL import Image


def overlay(original_image_path):

    # This is the image the user sends through text.
    background = Image.open(original_image_path)

    # Resizes the image received so that the height is always 1024px.
    baseheight = 1024 
    hpercent = (baseheight / float(background.size[1]))
    wsize = int((float(background.size[0]) * float(hpercent)))
    background = background.resize((wsize, baseheight), PIL.Image.BILINEAR)

    overlay = Image.open('overlay.png')

    # Specifies what pokemon sprite is used.
    pkmn = Image.open('pokemon-go-images/mewtwo.png')

    background = background.convert('RGBA')
    overlay = overlay.convert('RGBA')
    pkmn= pkmn.convert('RGBA')

    # Resize the overlay.
    overlay = overlay.resize(background.size, PIL.Image.BILINEAR);

    new_img = background
    new_img.paste(overlay, (0, 0), overlay)

    # Place the pokemon sprite centered on the background+overlay image.
    new_img.paste(pkmn, (background.size[0]/2, background.size[1]/2), pkmn)

    new_img.save(original_image_path,'PNG')
