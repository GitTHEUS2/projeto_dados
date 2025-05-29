CREATE DATABASE vendas;

USE vendas;

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,  
    nome_produto VARCHAR(100) NOT NULL,        
    categoria VARCHAR(50),                     
    preco DECIMAL(10, 2) NOT NULL              
);

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,  
    nome_cliente VARCHAR(100) NOT NULL,        
    cidade VARCHAR(50),                        
    estado VARCHAR(2)                          
);

CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,   
    id_produto INT,                           
    id_cliente INT,                           
    data_venda DATE NOT NULL,                 
    quantidade INT NOT NULL,                 
    valor_total DECIMAL(10, 2) NOT NULL,      
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),  
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)  
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