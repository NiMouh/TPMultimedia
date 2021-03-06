from PIL import Image


def adicao(primeira_imagem, segunda_imagem):

    # Inicializa a imagem em branco
    adicao_imagem = Image.new(primeira_imagem.mode, primeira_imagem.size, 'White')

    for i in range(0, adicao_imagem.width):
        for j in range(0, adicao_imagem.height):
            # Obtém o píxel das imagens originais
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            R = pixel1[0] + pixel2[0]
            if R > 255:
                R = 255

            G = pixel1[1] + pixel2[1]
            if G > 255:
                G = 255

            B = pixel1[2] + pixel2[2]
            if B > 255:
                B = 255

            # Coloca o pixel na imagem
            adicao_imagem.putpixel((i, j), (R, G, B))

    # Guarda a imagem
    adicao_imagem.save("Imagens/adicao.jpg")


def subtracao(primeira_imagem, segunda_imagem):

    # Inicializa a imagem em branco
    subtracao_imagem = Image.new(primeira_imagem.mode, primeira_imagem.size, 'White')

    for i in range(0, subtracao_imagem.width):
        for j in range(0, subtracao_imagem.height):
            # Obtém o píxel das imagens originais
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            R = pixel1[0] - pixel2[0]
            if R < 0:
                R = 0

            G = pixel1[1] - pixel2[1]
            if G < 0:
                G = 0

            B = pixel1[2] - pixel2[2]
            if B < 0:
                B = 0

            # Coloca o pixel na imagem
            subtracao_imagem.putpixel((i, j), (R, G, B))

    # Guarda a imagem
    subtracao_imagem.save("Imagens/subtracao.jpg")


def and_imagem(primeira_imagem, segunda_imagem):

    # Inicializa a imagem em branco
    and_img = Image.new(primeira_imagem.mode, primeira_imagem.size, 'White')

    for i in range(0, and_img.width):
        for j in range(0, and_img.height):
            # Obtém o píxel das imagens originais
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            pixel3 = tuple(pixel1 & pixel2 for pixel1, pixel2 in zip(pixel1, pixel2))

            # Coloca o pixel na imagem
            and_img.putpixel((i, j), pixel3)

    # Guarda a imagem
    and_img.save("Imagens/and.jpg")


def or_imagem(primeira_imagem, segunda_imagem):

    # Inicializa a imagem em branco
    or_img = Image.new(primeira_imagem.mode, primeira_imagem.size, 'White')

    for i in range(0, or_img.width):
        for j in range(0, or_img.height):
            # Obtém o píxel das imagens originais
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            pixel3 = tuple(pixel1 | pixel2 for pixel1, pixel2 in zip(pixel1, pixel2))

            # Coloca o pixel na imagem
            or_img.putpixel((i, j), pixel3)

    # Guarda a imagem
    or_img.save("Imagens/or.jpg")


def xor_imagem(primeira_imagem, segunda_imagem):

    # Inicializa a imagem em branco
    xor_img = Image.new(primeira_imagem.mode, primeira_imagem.size, 'White')

    for i in range(0, xor_img.width):
        for j in range(0, xor_img.height):
            # Obtém o píxel das imagens originais
            pixel1 = primeira_imagem.getpixel((i, j))
            pixel2 = segunda_imagem.getpixel((i, j))

            pixel3 = tuple(pixel1 ^ pixel2 for pixel1, pixel2 in zip(pixel1, pixel2))

            # Coloca o pixel na imagem
            xor_img.putpixel((i, j), pixel3)

    # Guarda a imagem
    xor_img.save("Imagens/xor.jpg")


def preto_e_branco(imagem):

    # Inicializa a imagem em branco
    preto_branco_img = Image.new(imagem.mode, imagem.size, 'White')

    for i in range(0, preto_branco_img.width):
        for j in range(0, preto_branco_img.height):
            # Obtém o píxel da imagem original
            pixel1 = imagem.getpixel((i, j))

            R = pixel1[0]
            G = pixel1[1]
            B = pixel1[2]

            bw = int((R + B + G) / 3)

            # Coloca o pixel na imagem
            preto_branco_img.putpixel((i, j), (bw, bw, bw))

    # Guarda a imagem
    preto_branco_img.save("Imagens/pretoebranco.jpg")


def negativo(imagem):

    # Inicializa a imagem em branco
    negativo_img = Image.new(imagem.mode, imagem.size, 'White')

    for i in range(0, negativo_img.width):
        for j in range(0, negativo_img.height):
            # Obtém o píxel da imagem original
            pixel1 = imagem.getpixel((i, j))

            R = 255 - pixel1[0]
            G = 255 - pixel1[1]
            B = 255 - pixel1[2]

            # Coloca o pixel na imagem
            negativo_img.putpixel((i, j), (R, G, B))

    # Guarda a imagem
    negativo_img.save("Imagens/negativo.jpg")


def invertida_horizontal(imagem):

    # Inicializa a imagem em branco
    invertida_img = Image.new(imagem.mode, imagem.size, 'White')

    for i in range(0, invertida_img.width):
        for j in range(0, invertida_img.height):
            # Obtém o píxel da imagem original
            pixel1 = imagem.getpixel((i, j))
            ip = (imagem.width - i) - 1

            # Coloca o pixel na imagem
            invertida_img.putpixel((ip, j), pixel1)

    # Guarda a imagem
    invertida_img.save("Imagens/invertida_horizontal.jpg")


def invertida_vertical(imagem):

    # Inicializa a imagem em branco
    invertida_img = Image.new(imagem.mode, imagem.size, 'White')

    for i in range(0, invertida_img.width):
        for j in range(0, invertida_img.height):
            # Obtém o píxel da imagem original
            pixel1 = imagem.getpixel((i, j))
            jp = (imagem.height - j) - 1

            # Coloca o pixel na imagem
            invertida_img.putpixel((i, jp), pixel1)

    # Guarda a imagem
    invertida_img.save("Imagens/invertida_vertical.jpg")


def menu():
    print("\n           # Bem-vindo à edição de imagens #")
    print("===========================================================")
    print("1 -> Fazer adição entre 2 imagens.")
    print("2 -> Fazer subtração entre 2 imagens.")
    print("3 -> Fazer AND lógico entre 2 imagens.")
    print("4 -> Fazer OR lógico entre 2 imagens.")
    print("5 -> Fazer XOR lógico entre 2 imagens.")
    print("6 -> Transformar uma imagem a cores numa em preto e branco.")
    print("7 -> Transformar uma imagem no seu negativo.")
    print("8 -> Transformar uma imagem no seu inverso.(horizontalmente)")
    print("9 -> Transformar uma imagem no seu inverso (verticalmente).")
    print("10-> Comprimir uma imagem.")
    print("0 -> Terminar.\n")
    escolha = int(input("Escolha uma opção: "))
    return escolha


if __name__ == "__main__":
    opcao = menu()

    # Inicializa as imagens
    imagem_primaria = Image.open("Imagens/image1.jpg")
    imagem_secundaria = Image.open("Imagens/image2.jpg")
    imagem_terciaria = Image.open("Imagens/image3.jpg")

    while opcao != 0:
        if opcao == 1:
            adicao(imagem_primaria, imagem_secundaria)
            print("Operação 1 foi concluída.")
        elif opcao == 2:
            subtracao(imagem_primaria, imagem_secundaria)
            print("Operação 2 foi concluída.")
        elif opcao == 3:
            and_imagem(imagem_primaria, imagem_secundaria)
            print("Operação 3 foi concluída.")
        elif opcao == 4:
            or_imagem(imagem_primaria, imagem_secundaria)
            print("Operação 4 foi concluída.")
        elif opcao == 5:
            xor_imagem(imagem_primaria, imagem_secundaria)
            print("Operação 5 foi concluída")
        elif opcao == 6:
            preto_e_branco(imagem_primaria)
            print("Operação 6 foi concluída.")
        elif opcao == 7:
            negativo(imagem_terciaria)
            print("Operação 7 foi concluída.")
        elif opcao == 8:
            invertida_horizontal(imagem_primaria)
            print("Operação 8 foi concluída.")
        elif opcao == 9:
            invertida_vertical(imagem_primaria)
            print("Operação 9 foi concluída.")
        elif opcao == 10:
            qualidade = int(input("Defina a qualidade da imagem: "))
            imagem_primaria.save("comprimida.jpg", optimize=True, quality=qualidade)
            print("Operação 10 foi concluída.")
        else:
            print("Opção inválida.")

        # Volta a printar o menu
        opcao = menu()
    print("Encerrando...")
