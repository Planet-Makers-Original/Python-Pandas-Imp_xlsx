# bibliotecas
import os # manipular arquivos e diretorio
import pandas as pd # manipular dados

# caminhos para a diretorio com aquivos
diretorio = r"/home/master/Pojects/Pandas/Python-Pandas/data"

# listagem de todos arquivos dento dos diretorio
arquivos = [os.path.join(diretorio, arquivo) for arquivo in os.listdir(diretorio)]

# lista todas as planilhas
#print(arquivos)

# primeia planilha[0], segunda planilha[1] e assim por diante
# index_col=0, é o index da planilha ou index_col="nome da coluna: 0"
#tabela_resultado = pd.read_excel(arquivos[1], index_col=0)
#print(tabela_resultado)

# tabela inicia vazia
tabela_resultado = pd.DataFrame()

# loop para ler cada planilha e criar uma linha na tabela
for arquivo in arquivos:
  # lê o arquivo
  df = pd.read_excel(arquivo, index_col=0)
  # adiciona registro na tabela
  tabela_resultado = pd.concat([tabela_resultado, df])
# exporta tabela para uma planilha do Excel
tabela_resultado.to_excel("tabela_resultado_2021_2024.xlsx") # sem index