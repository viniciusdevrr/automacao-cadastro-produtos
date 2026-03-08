# Automação de Cadastro de Produtos

Projeto de automação desenvolvido em Python para realizar o cadastro automático de produtos em um sistema.

O objetivo do projeto é automatizar tarefas repetitivas, reduzindo tempo de trabalho manual e aumentando a produtividade no cadastro de dados.

## Funcionalidades

* Automação de tarefas repetitivas
* Preenchimento automático de formulários
* Leitura de dados a partir de arquivos
* Cadastro automático de múltiplos produtos

## Tecnologias Utilizadas

* Python
* PyAutoGUI
* Pandas

## Como Executar

### 1. Clonar o repositório

```shell
git clone https://github.com/viniciusdevrr/automacao-cadastro-produtos.git
```

### 2. Instalar dependências

```shell
pip install -r requirements.txt
```

### 3. Configurar as coordenadas do mouse

Este projeto utiliza automação com **PyAutoGUI**, portanto as posições do mouse dependem da resolução da tela.

Antes de executar o script principal, é necessário identificar as coordenadas corretas dos campos da interface.

Execute o código abaixo duas vezes para capturar a posição do mouse ( x , y ) nos campos Email e Código do Produto:

```python
import time
import pyautogui

time.sleep(5)
print(pyautogui.position())
```

Passo a Passo:

1. Execute o script acima - posicao_mouse.py
2. Entre na interface.html
3. Posicione o mouse sobre o campo da interface E-mail ou Código do Produto
3. Aguarde 5 segundos
4. Copie as coordenadas exibidas no terminal
5. Substitua os valores no código principal - automacao.py

Exemplo no E-mail:

```python
pyautogui.click(x=1111, y=222)
pyautogui.write("emailteste@gmail.com")
```
Exemplo no Código do Produto:

```python
for linha in tabela.index:
pyautogui.click(x=3333, y=444)
# Preenche os requisitos de cada produto
codigo = str(tabela.loc[linha, "codigo"])
```


Observação:
As coordenadas utilizadas no projeto foram capturadas em uma resolução específica de tela.
Caso o projeto seja executado em outro computador, será necessário ajustar as posições do mouse.

### 4. Executar o script

```bash
python cadastro_automatico.py
```

## Objetivo do Projeto

Aplicar conceitos de automação de tarefas utilizando Python para otimizar processos repetitivos.
