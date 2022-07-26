import pyautogui  # pacote de automatização
import pyperclip  # copiar e cola
import time       # define um tempo

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyperclip.copy(
    "https://outlook.live.com/mail/0/")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

pyautogui.click(x=-1740, y=182, clicks=1)
time.sleep(3)
pyautogui.click(x=-1090, y=234, clicks=1)
pyperclip.copy(
    "gabriel.ap.almeida@outlook.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.click(x=-1171, y=289, clicks=1)
pyautogui.write("ESSE É UM EMAIL TESTE ENVIADO AUTOMATICO")
pyautogui.press("tab")
pyautogui.write("Boa noite,")
pyautogui.press("enter")
pyautogui.write(
    "Esse é um email teste enviado de forma automática utilizando python.")
pyautogui.click(x=-1162, y=675, clicks=1)


# Passo 3: Download da base de dados
# Passo 4: Calcular os indicadores(faturamento, quantidade de produtos)
# Passo 5: Entrar no email
# Passo 6: Manda um email para diretoria
#-----------------------------------------------------------------------------------------------------#
