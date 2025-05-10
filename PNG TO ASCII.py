from PIL import Image

def converter_png_para_ascii(caminho_da_imagem, largura=100, caracteres=None):
    """
    Converte uma imagem PNG para arte ASCII.

    Args:
        caminho_da_imagem (str): O caminho para o arquivo de imagem PNG.
        largura (int): A largura desejada da arte ASCII (a altura será ajustada proporcionalmente).
        caracteres (str ou list): Uma string ou lista de caracteres para usar na arte ASCII,
                                   ordenados do mais escuro para o mais claro.
                                   Se None, usa uma lista padrão.

    Returns:
        str: Uma string representando a arte ASCII da imagem.
             Retorna None se a imagem não puder ser aberta.
    """
    try:
        imagem = Image.open(caminho_da_imagem).convert('L') 
    except FileNotFoundError:
        print(f"Erro: A imagem '{caminho_da_imagem}' não foi encontrada.")
        return None
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return None

    largura_original, altura_original = imagem.size
    proporcao = altura_original / largura_original
    nova_altura = int(largura * proporcao)
    imagem_redimensionada = imagem.resize((largura, nova_altura))
    pixels = imagem_redimensionada.getdata()

    if caracteres is None:
        caracteres = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    elif isinstance(caracteres, str):
        caracteres = list(caracteres)

    num_niveis = len(caracteres)
    intervalo_por_nivel = 256 / num_niveis

    pixels_para_caracteres = [caracteres[int(pixel / intervalo_por_nivel)] for pixel in pixels]
    arte_ascii = [pixels_para_caracteres[i:i + largura] for i in range(0, len(pixels_para_caracteres), largura)]
    return "\n".join("".join(linha) for linha in arte_ascii)

if __name__ == "__main__":
    caminho_da_imagem = input("Digite o caminho da imagem PNG: ")
    largura_desejada = int(input("Digite a largura desejada para a arte ASCII (padrão: 100): ") or 100)
    caracteres_personalizados = input("Digite uma string de caracteres para usar (opcional, do mais escuro para o mais claro): ") or None

    arte = converter_png_para_ascii(caminho_da_imagem, largura_desejada, caracteres_personalizados)

    if arte:
        print("\nArte ASCII gerada:\n")
        print(arte)

        
        salvar = input("\nDeseja salvar a arte ASCII em um arquivo de texto? (s/n): ").lower()
        if salvar == 's':
            nome_arquivo = input("Digite o nome do arquivo para salvar (ex: arte.txt): ")
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write(arte)
            print(f"\nArte ASCII salva em '{nome_arquivo}'")