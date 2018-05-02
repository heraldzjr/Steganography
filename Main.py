import encrypt
from PIL import Image
import  decrypt

def encoded_banda(option, imgname):

    encoded_image_file = ""

    if option == 1:
        encoded_image_file = "enc_1_" + original_image_file
    elif option == 2:
        encoded_image_file = "enc_2_" + original_image_file
    elif option == 3:
        encoded_image_file = "enc_3_" + original_image_file

    return encoded_image_file

if __name__ == '__main__':

    init = int(input("Digite a opção desejada: \n1 - Encriptar Imagem;\n2 - Decriptar Imagem;\nOpção: "))

    if init == 1:
        original_image_file = input("Insira o nome da imagem: ")
        img = Image.open(original_image_file)
        print(img, img.mode)  # test
        # create a new filename for the modified/encoded image
        option = int(input("Digite a banda: "))
        encoded_image_file = encoded_banda(option, original_image_file)
        # don't exceed 255 characters in the message
        file_path = input("Insira o nome do arquivo com a mensagem: ")
        file = open(file_path, "r")
        secret_msg = file.read()

        print(len(secret_msg))  # test
        img_encoded = encrypt.encode_image(img, secret_msg, option)

        if img_encoded:
            # save the image with the hidden text
            img_encoded.save(encoded_image_file)
            print("{} saved!".format(encoded_image_file))

    elif init == 2:
            print(
                "Se a imagem estiver na mesma pasta do código, digite apenas o nome da imagem com a extensão\nCaso contrario, digite o caminha completo da imagem")
            encoded_image_file = input("Digite a imagem: ")

            img2 = Image.open(encoded_image_file)
            origin_file = input("Digite o nome do arquivo: ")
            file = open(origin_file, "w")

            option = int(input("Selecione uma das bandas para decriptar:\n 1 - Red;\n 2 - Green;\n 3 - Blue;\nOpção: "))
            hidden_text = decrypt.decode_image(img2, option)
            print(hidden_text)
            write = encoded_image_file + " - " + hidden_text
            print(write)

            # Verifica se há mensagem oculta, caso haja, ela é apresentada caso
            # contrario, aparecce a mensagem: "Sem mensagem oculta!"
            if decrypt.is_ascii(hidden_text) == True:
                print("Hidden text:\n{}".format(hidden_text))
                file.write(write)
                file.close()
            elif decrypt.is_ascii(hidden_text) == False:
                print("Sem mensagem oculta!")




