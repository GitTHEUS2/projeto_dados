import mysql.connector
from faker import Faker
import random

# Configurar Faker para dados em português do Brasil
fake = Faker('pt_BR')

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",       # Endereço do servidor MySQL
    user="root",     # Nome de usuário do MySQL
    password="Projeto@2025",   # Senha do MySQL
    database="vendas"       # Nome do banco de dados
)
cursor = conn.cursor()

# Lista de categorias de produtos
categorias = ['Eletrônicos', 'Móveis', 'Roupas', 'Alimentos']

# Gerar e inserir dados de produtos
for _ in range(20):  # 20 produtos
    nome_produto = fake.word().capitalize() + ' ' + fake.word().capitalize()
    categoria = random.choice(categorias)
    preco = round(random.uniform(50, 1000), 2)
    cursor.execute('''
    INSERT INTO produtos (nome_produto, categoria, preco)
    VALUES (%s, %s, %s)
    ''', (nome_produto, categoria, preco))

# Gerar e inserir dados de clientes
for _ in range(60):  # 60 clientes
    nome_cliente = fake.name()
    cidade = fake.city()
    estado = fake.estado_sigla()
    cursor.execute('''
    INSERT INTO clientes (nome_cliente, cidade, estado)
    VALUES (%s, %s, %s)
    ''', (nome_cliente, cidade, estado))

# Gerar e inserir dados de vendas
for _ in range(2097):  # 2000 vendas
    id_produto = random.randint(1, 20)
    id_cliente = random.randint(1, 60)
    data_venda = fake.date_between(start_date='-1y', end_date='today')
    quantidade = random.randint(1, 5)
    cursor.execute('SELECT preco FROM produtos WHERE id_produto = %s', (id_produto,))
    preco = cursor.fetchone()[0]
    valor_total = round(quantidade * preco, 2)
    cursor.execute('''
    INSERT INTO vendas (id_produto, id_cliente, data_venda, quantidade, valor_total)
    VALUES (%s, %s, %s, %s, %s)
    ''', (id_produto, id_cliente, data_venda, quantidade, valor_total))

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Dados fictícios inseridos no banco de dados com sucesso!")