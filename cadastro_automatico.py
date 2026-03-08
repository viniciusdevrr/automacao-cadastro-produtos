"""
Automação de cadastro de produtos utilizando PyAutoGUI.

O script abre uma interface HTML local, realiza login automaticamente
e cadastra produtos a partir de um arquivo CSV.

Observação:
As coordenadas X e Y utilizadas são relativas à resolução da tela do computador.
"""

import pyautogui
import time
import os
import webbrowser
import pandas

# Define uma pausa automática entre os comandos do pyautogui
pyautogui.PAUSE = 0.5

# Abre a interface HTML utilizada para o cadastro - Como um exemplo de sistema de empresa
caminho_html = os.path.abspath("interface/interface.html")
url = "file:///" + caminho_html.replace("\\", "/")
webbrowser.open(url)

# Aguarda o carregamento da página
time.sleep(2)

# Realiza o login no sistema
# Lembrando que essas cordenadas de X e Y representam uma resolução específica de tela
# Leia o README.md antes de executar
pyautogui.click(x=2526, y=258)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234asdf")

pyautogui.press("tab")
pyautogui.press("enter")

# Aguarda o sistema abrir após o login
time.sleep(3)

# Lê a tabela de produtos que será utilizada para cadastro
tabela = pandas.read_csv("produtos.csv")

# Percorre cada produto da tabela e realiza o cadastro automático
for linha in tabela.index:

    pyautogui.click(x=2526, y=254)

    # Preenche os requisitos de cada produto
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    # Envia o cadastro do produto
    pyautogui.press("enter")

    # Rola a página para visualizar o próximo cadastro
    pyautogui.scroll(5000)