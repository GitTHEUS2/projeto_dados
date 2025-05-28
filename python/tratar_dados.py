import mysql.connector
import pandas as pd
import os

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Projeto@2025",
    database="vendas"
)

# Extrair dados das tabelas
query_produtos = "SELECT * FROM produtos"
query_clientes = "SELECT * FROM clientes"
query_vendas = "SELECT * FROM vendas"

df_produtos = pd.read_sql(query_produtos, conn)
df_clientes = pd.read_sql(query_clientes, conn)
df_vendas = pd.read_sql(query_vendas, conn)

# Fechar conexão
conn.close()

# Tratamento de Dados
# Substituir valores nulos na coluna 'categoria' da tabela produtos
df_produtos['categoria'] = df_produtos['categoria'].fillna('Outros')

# Converter a coluna 'data_venda' para o tipo datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Remover duplicatas na tabela clientes (baseado no nome do cliente)
df_clientes = df_clientes.drop_duplicates(subset=['nome_cliente'])

# Definir o caminho absoluto para salvar os arquivos
caminho_salvar = "C:/Users/mathe/Desktop/Projeto Dash 2025/Python/"

# Salvar dados tratados em CSV
df_produtos.to_csv(os.path.join(caminho_salvar, 'produtos_tratados.csv'), index=False)
df_clientes.to_csv(os.path.join(caminho_salvar, 'clientes_tratados.csv'), index=False)
df_vendas.to_csv(os.path.join(caminho_salvar, 'vendas_tratadas.csv'), index=False)

print(f"Dados tratados e salvos em CSV na pasta: {caminho_salvar}")