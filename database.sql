DROP DATABASE IF EXISTS hexadatabase;
CREATE DATABASE hexadatabase;
USE hexadatabase;


DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
    id_cliente INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    sobrenome VARCHAR(30) NOT NULL,
    instagram varchar(30) NOT NULL,
    CPF INT NOT NULL UNIQUE,
    PRIMARY KEY (id_cliente)
);

DROP TABLE IF EXISTS enderecos;
CREATE TABLE enderecos (
	id_endereco INT NOT NULL AUTO_INCREMENT,
    CEP INT NOT NULL UNIQUE,
    rua VARCHAR(45) NOT NULL,
    numero INT NOT NULL,
    complemento INT,
    id_cliente INT NOT NULL,
    PRIMARY KEY (id_endereco),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

DROP TABLE IF EXISTS carrinhos;
CREATE TABLE carrinhos(
	id_carrinho INT NOT NULL AUTO_INCREMENT,
    valor FLOAT NOT NULL,
    pago TINYINT NOT NULL,
    entregue TINYINT NOT NULL,
    id_cliente INT NOT NULL,
    finalizado INT NOT NULL,
    frete FLOAT NOT NULL,
    PRIMARY KEY (id_carrinho),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);


DROP TABLE IF EXISTS itens;
CREATE TABLE itens(
	id_item INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR (45) NOT NULL,
    valor INT NOT NULL,
    descricao MEDIUMTEXT NOT NULL,
    PRIMARY KEY (id_item)
);


DROP TABLE IF EXISTS carrinho_tem_item;
CREATE TABLE carrinhos_tem_itens(
	id_carrinhoItem INT NOT NULL AUTO_INCREMENT,
    feito TINYINT NOT NULL,
    lixado TINYINT NOT NULL,
    id_carrinho INT NOT NULL,
    id_item INT NOT NULL,
    PRIMARY KEY(id_carrinhoItem),
    FOREIGN KEY (id_carrinho) REFERENCES carrinhos(id_carrinho),
    FOREIGN KEY (id_item) REFERENCES itens(id_item)
);



INSERT INTO clientes(nome, sobrenome,instagram, CPF ) VALUES ('Micah','Zassim', "@micah_zassim", 1233456), ('Flip','Liporg', "@flip_liporg", 223454556), ('Adin', 'Samura', "@adin_samura", 23444555);
INSERT INTO enderecos(CEP, rua,numero,complemento, id_cliente) VALUES (333444,"rua da micah", 33, 207, 1), (4444,"Rua do flip", 4,0,2);
INSERT INTO carrinhos(valor, pago,entregue,id_cliente, finalizado, frete) VALUES (204.2,1, 0, 1, 1, 21.3);
INSERT INTO itens(nome, valor, descricao) VALUES ("hexadados",120,"Esse dado e transparente, com cores rosas bebe dentro e nummeros precos ao redor");
INSERT INTO carrinhos_tem_itens(feito,lixado,id_carrinho, id_item) VALUES (1,0,1,1);
