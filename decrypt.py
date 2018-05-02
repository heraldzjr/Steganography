from PIL import Image

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def decode_image(img, option):
    """
    Verifica as bandas da imagem (r, g, b) para
     tentar encontrar uma mensagem oculta (ASCII)
    """
    width, height = img.size
    msg = ""
    index = 0

    # option == 1; red

    if option == 1:
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))
                # first pixel r value is length of message
                if row == 0 and col == 0:
                    length = r
                elif index <= length:
                    msg += chr(r)
                index += 1

    # option == 2; green;
    elif option == 2:
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))
                # first pixel g value is length of message
                if row == 0 and col == 0:
                    length = g
                elif index <= length:
                    msg += chr(g)
                index += 1

    # option == 3; blue;
    elif option == 3:
        for row in range(height):
            for col in range(width):
                try:
                    r, g, b = img.getpixel((col, row))
                except ValueError:
                    # need to add transparency a for some .png files
                    r, g, b, a = img.getpixel((col, row))
                # first pixel b value is length of message
                if row == 0 and col == 0:
                    length = b
                elif index <= length:
                    msg += chr(b)
                index += 1
    return msg