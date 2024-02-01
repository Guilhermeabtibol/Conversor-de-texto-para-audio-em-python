from gtts import gTTS
import os
import PyPDF2
import pygame

def extrair_texto(pdf_path):
    texto = ""
    with open(pdf_path, 'rb') as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        num_paginas = len(leitor_pdf.pages)

        for pagina_num in range(num_paginas):
            pagina = leitor_pdf.pages[pagina_num]
            texto += pagina.extract_text()

    return texto

def texto_para_voz(texto, arquivo_saida="output.mp3"):
    tts = gTTS(text=texto, lang='pt')
    tts.save("output.mp3")
    print(f"Áudio salvo em: {arquivo_saida}")

def reproduzir_audio(arquivo):
    pygame.mixer.init()
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

if __name__ == "__main__":
    pdf_path = r"o diretorio do seu livro em .pdf"
    texto_extraido = extrair_texto(pdf_path)

    print("Texto extraído do PDF:")
    print(texto_extraido)

    nome_arquivo_audio =  r"o diretorio da pasta onde vc quer o seu audio\output.mp3"
    print("Convertendo texto em áudio... e salvando em {nome_arquivo}")
    texto_para_voz(texto_extraido, nome_arquivo_audio)

    print("Reproduzindo áudio")
    reproduzir_audio(nome_arquivo_audio)
