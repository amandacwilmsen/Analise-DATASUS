# Importe as bibliotecas necessárias, 
import pandas as pd

# Import PYSUS, biblioteca utilizada para acessar dados do SUS
from pysus.online_data.SIM import download

# Coloquei poucas opcoes para o processo de desenvolvimento
estados = ["AL"]
anos = [2014]
banco={}
for y in anos:
 for uf in estados: 
    banco[uf, y] = download(states=uf, years=y, groups="CID9")
    print("Banco de " + str(y) + " de " + str(uf) + " baixado!")

# Exemplo
dados = banco['AL', 2014]

# Converta os dados em um DataFrame
dados = pd.DataFrame(dados)