-- Cria o banco de dados 'vendas'
CREATE DATABASE vendas;

-- Usa o banco de dados 'vendas'
USE vendas;

-- Tabela Produtos
CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,  -- Chave primária
    nome_produto VARCHAR(100) NOT NULL,        -- Nome do produto (não pode ser nulo)
    categoria VARCHAR(50),                     -- Categoria do produto
    preco DECIMAL(10, 2) NOT NULL              -- Preço do produto (não pode ser nulo)
);

-- Tabela Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,  -- Chave primária
    nome_cliente VARCHAR(100) NOT NULL,        -- Nome do cliente (não pode ser nulo)
    cidade VARCHAR(50),                        -- Cidade do cliente
    estado VARCHAR(2)                          -- Estado do cliente (sigla de 2 caracteres)
);

-- Tabela Vendas
CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,   -- Chave primária
    id_produto INT,                           -- Chave estrangeira para a tabela 'produtos'
    id_cliente INT,                           -- Chave estrangeira para a tabela 'clientes'
    data_venda DATE NOT NULL,                 -- Data da venda (não pode ser nula)
    quantidade INT NOT NULL,                  -- Quantidade vendida (não pode ser nula)
    valor_total DECIMAL(10, 2) NOT NULL,      -- Valor total da venda (não pode ser nulo)
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),  -- Chave estrangeira
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)   -- Chave estrangeira
);

INSERT INTO produtos (nome_produto, categoria, preco)
VALUES ('Notebook Dell', 'Eletrônicos', 3500.00);

INSERT INTO clientes (nome_cliente, cidade, estado)
VALUES ('João Silva', 'São Paulo', 'SP');

INSERT INTO vendas (id_produto, id_cliente, data_venda, quantidade, valor_total)
VALUES (1, 1, '2023-10-01', 2, 7000.00);

SELECT * FROM produtos;

SELECT * FROM vendas;

SELECT * FROM clientes;