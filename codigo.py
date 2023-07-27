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
pyautogui.click(x=693, y=532) # clique no botão de login
time.sleep(2)

# Passo 3: Importar a vitordavidps@gmail.com    sua senha de produtos pra cadastrar
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=728, y=249)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # Passar para o próximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): # O .insna() verificar se o campo está vazio.
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar um sroll pra cima
    pyautogui.scroll(500)

# Passo 5: Repetir o processo de cadastro até o fim


