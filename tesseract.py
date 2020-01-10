#          Recomendações tesseract OCR
# Dois canais de cores somente (preto e branco)
# Texto alinhado/padronizado e sem ruídos
# Altura do box (espaço ocupado pelos caracteres) superior ao mínimo de 10px
# Densidade ideal de 300dpi, ou proporcionais para o pressuposto acima
# Possuir o texto extraível em um único padrão de alfabeto (ou idioma)
# Sem espaço inútil, considerado como bordas para o texto

import pytesseract as ocr
import numpy as np
import cv2 #pip install opencv-python

from PIL import Image

# tipando a leitura para os canais de ordem RGB
imagem = Image.open('nome.png').convert('RGB')

# convertendo em um array editável de numpy[x, y, CANALS]
npimagem = np.asarray(imagem).astype(np.uint8)  

# diminuição dos ruidos antes da binarização
npimagem[:, :, 0] = 0 # zerando o canal R (RED)
npimagem[:, :, 2] = 0 # zerando o canal B (BLUE)

# atribuição em escala de cinza
im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 

# aplicação da truncagem binária para a intensidade
# pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
# pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
# A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
binimagem = Image.fromarray(thresh) 

# salva imagem para verificação
binimagem.save("nova.jpg") 


# ERRO tesseract is not installed or it's not in your path
# Especifica pasta de do arquivo exe do tesseract instalado
ocr.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'

# chamada ao tesseract OCR por meio de seu wrapper
phrase = ocr.image_to_string(binimagem, lang='por')

# impressão do resultado
print(phrase) 
