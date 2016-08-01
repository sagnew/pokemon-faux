from PIL import Image


def overlay(original_image_path, pokemon):

    overlay_image = Image.open('overlay.png')

    # This is the image the user sends through text.
    background = Image.open(original_image_path)

    # Resizes the image received so that the height is always 512px.
    base_height = 512
    height_percent = base_height / background.size[1]
    width = int(background.size[0] * height_percent)
    background = background.resize((width, base_height), Image.BILINEAR)

    # Resize the overlay.
    overlay_image = overlay_image.resize(background.size, Image.BILINEAR)

    # Specify which pokemon sprite is used.
    pokemon_img = Image.open('pokemon-go-images/{}.png'.format(pokemon))

    # Convert images to RGBA format.
    background = background.convert('RGBA')
    overlay_image = overlay_image.convert('RGBA')
    pokemon_img = pokemon_img.convert('RGBA')

    new_img = background
    new_img.paste(overlay_image, (0, 0), overlay_image)

    # Place the pokemon sprite centered on the background + overlay image.
    new_img.paste(pokemon_img,
                  (int(width / 4), int(base_height / 4)),
                  pokemon_img)

    # Save the new image.
    new_img.save(original_image_path,'PNG')
