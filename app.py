# INTENSIVÃO DE PYTHON - HASHTAG PROGRAMAÇÃO
# press -> tecla do teclado
# write -> digitar

# biblioteca - pip install pyautogui
import pyautogui  # pacote de automatização
import pyperclip  # copiar e cola
import time       # define um tempo

pyautogui.PAUSE = 1
#-----------------------------------------------------------------------------------------------------#
# Passo 1: Entrar no sistema da empresa (entrar no link do drive)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyperclip.copy(
    "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
# Passo 2: Navegar dentro do sistema e encontrar a base de dados (entrar na pasta exportar)
time.sleep(5)
pyautogui.click(x=-1564, y=309, clicks=2)

# Passo 3: Download da base de dados
# Passo 4: Calcular os indicadores(faturamento, quantidade de produtos)
# Passo 5: Entrar no email
# Passo 6: Manda um email para diretoria
#-----------------------------------------------------------------------------------------------------#
