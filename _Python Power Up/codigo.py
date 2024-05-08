import pyautogui
import time
import pandas as pd

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # Site para teste

pyautogui.PAUSE = 0.5 # Configura um tempo de espera de 0,5 segundos apos cada comando

# Abre o google chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Acessa o site
pyautogui.write(site) 
pyautogui.press("enter")
time.sleep(1) # Tempo de espera para abrir o site

# Preenche o login do site
# pyautogui.click(x=731, y=407) # Clica
pyautogui.press("tab")
pyautogui.write("teste@gmail.com") # Coloque aqui seu login
pyautogui.press("tab")
pyautogui.write("senha54321") # Coloque aqui sua senha
pyautogui.press("enter")

# Acessa a tabela e preenche os campos dos produtos
tabela = pd.read_csv("produtos.csv")
for x in tabela.index:
    pyautogui.click(x=547, y=296)
    for y in tabela.columns:
        if tabela.loc[x,y] != "nan":
            pyautogui.write(str(tabela.loc[x,y]))
        pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")

