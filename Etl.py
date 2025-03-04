import requests
import pandas as pd
from sqlalchemy import create_engine
# URL da API
url = "https://api.coinpaprika.com/v1/tickers"

# Fazer a requisição
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
else:
    print("Erro ao acessar API:", response.status_code)
# Criar DataFrame com as principais colunas
df = pd.DataFrame(data)[['id', 'name', 'symbol', 'rank', 'quotes']]
df['price_usd'] = df['quotes'].apply(lambda x: x['USD']['price'])  # Extraindo o preço em USD
df = df.drop(columns=['quotes'])  # Removendo coluna desnecessária

# Exibir amostra dos dados
print(df.head())



# Configurar conexão com o MySQL
user = "root"
password = "4783"
host = "localhost"
database = "criptoDB"

engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")

# Carregar os dados no MySQL
df.to_sql("criptomoedas", con=engine, if_exists="replace", index=False)

print("Dados inseridos no MySQL com sucesso!")
