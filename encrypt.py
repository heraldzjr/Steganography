from PIL import Image
import Main

def encode_image(img, msg, option):

    length = len(msg)
    # limit length of message to 255
    if length > 255:
        print("text too long! (don't exceed 255 characters)")
        return False
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False

    encoded = img.copy()
    width, height = img.size
    index = 0

    if option == 1:
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = r
                encoded.putpixel((col, row), (asc, g , b))
                index += 1
    elif option == 2:
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = g
                encoded.putpixel((col, row), (r, asc , b))
                index += 1
    elif option == 3:
        for row in range(height):
            for col in range(width):
                r, g, b = img.getpixel((col, row))
                if row == 0 and col == 0 and index < length:
                    asc = length
                elif index <= length:
                    c = msg[index -1]
                    asc = ord(c)
                else:
                    asc = b
                encoded.putpixel((col, row), (r, g , asc))
                index += 1
    return encoded


