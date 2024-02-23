import sqlite3

turma = sqlite3.connect('tabela_alunos')
cursor = turma.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(111, "Juliana", 27, "Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(222, "Davi", 28, "Engenharia de Software")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(333, "Ana Clara", 25, "Analise de sistemas")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(444, "Giovana", 24, "Analise de sistemas")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(555, "José", 19, "Engenharia Mecânica")')

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
visualizar = cursor.execute('SELECT * FROM alunos')

for alunos in visualizar:
    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
visualizar = cursor.execute('SELECT nome, idade FROM alunos where idade>20')

for alunos in visualizar:
    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

visualizar = cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome DESC')

for alunos in visualizar:
    print(alunos)

#d) Contar o número total de alunos na tabela

visualizar = cursor.execute('SELECT COUNT(*) FROM alunos')

for alunos in visualizar:
    print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.

cursor.execute('UPDATE alunos SET idade = 22 WHERE nome = "Ana Clara"')

#b) Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos WHERE id = 444')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

cursor.execute('CREATE TABLE clientes(id INT, nome VARCHAR(100), idade INT, saldo FLOAT)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(111, "Antonio", 53, 1092.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(222, "Manuel", 41, 900.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(333, "Ana Clara", 22, 3000.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(444, "Juliana", 29, 42000.00)')



#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

visualizar = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

for clientes in visualizar:
    print(clientes)

#b) Calcule o saldo médio dos clientes.

visualizar = cursor.execute('SELECT AVG(saldo) FROM clientes')

for clientes in visualizar:
    print(clientes)

#c) Encontre o cliente com o saldo máximo.

visualizar = cursor.execute('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')

for clientes in visualizar:
   print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.

visualizar = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

for clientes in visualizar:
   print(clientes)

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.

cursor.execute('UPDATE clientes SET saldo = 2500 WHERE nome = "Antonio"')

#b) Remova um cliente pelo seu ID.

cursor.execute('DELETE FROM clientes WHERE id = 444')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.

cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(111, 111, "Computador", 4500.00)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(222, 222, "Fone de ouvido", 100.00)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(333, 333, "Teclado", 300.00)')
cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES(444, 444, "Monitor", 1550.00)')

visualizar = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')

for clientes in visualizar:
   print(clientes)

turma.commit()
turma.close()
