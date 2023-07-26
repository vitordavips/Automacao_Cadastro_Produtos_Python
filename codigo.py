# Passo 1: importar as bibliotecas
import pandas as pd
import time
import pyautogui

# https://dlp.hashtagtreinamentos.com/python/intensivao/login


pyautogui.PAUSE = 0.5

# abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=287, y=646, button='left')


# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Fazer login
#Selecionar o campo email
pyautogui.click(x=594, y=364)
# escrever o seu email
pyautogui.write("vitordavidps@gmail.com")
pyautogui.press("tab") # passando o próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=679, y=468) # clique no botão de login
