CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo INTEGER NOT NULL,
    nome TEXT NOT NULL,
    cargo TEXT NOT NULL,
    salario REAL NOT NULL,
    data_admissao TEXT NOT NULL
);

-- Inserir funcionários fictícios
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (001, 'Alice', 'Gerente', 7500.00, '01/01/2020');
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (002, 'Bob', 'Desenvolvedor', 5500.00, '15/03/2021');
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (003, 'Carlos', 'Designer', 4500.00, '10/06/2019');
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (004, 'Diana', 'Analista', 5000.00, '20/07/2022');
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (005, 'Eva', 'Auxiliar Administrativo', 3500.00, '05/10/2018');
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (006, 'Marquinhos', 'Auxiliar Administrativo', 3500.00, '05/10/2018');
INSERT INTO funcionarios (codigo, nome, cargo, salario, data_admissao) VALUES (007, 'James Bond', 'Auxiliar Administrativo', 3500.00, '05/10/2018');
