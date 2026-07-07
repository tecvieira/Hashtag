import pyautogui
import time

# bibbliotecas = pacotes de códigos prontos que podemos usar no nosso programa
#Passo a passo do seu programa
#passo1 entrar no sistema da empresa
#passo2 fazer login
#passo3 abrir base de dados
#passo4 cadastrar um produto
#passo5 repetir o passo 4 até acabar a lista de produtos
pyautogui.pause = 0.5
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# fazer uma pausa de 2 segundos para o navegador abrir
time.sleep(3)
pyautogui.click(x=647, y=447)
pyautogui.write("https://www.sistemaempresa.com")
pyautogui.press("enter")