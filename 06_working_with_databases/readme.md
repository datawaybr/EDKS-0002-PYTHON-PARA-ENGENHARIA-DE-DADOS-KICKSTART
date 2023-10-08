# Trabalhando com bancos de dados

## Ferrametas utilizadas

- [Dbeaver](https://dbeaver.io/)
- [Sqlite3](https://www.sqlite.org/index.html)
- [Postgres](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

### Sqlite3

O python já vem com o módulo `sqlite3` instalado, então não é necessário instalar nada.

### Postgres

Vamos utilizar uma instalação do Postgres dentro de um container Docker. 

Vamos fazer o passo a passo aqui, mas caso tenha dúvidas de como usar o docker, sugerimos que revise a formação BS-0003 - DOCKER PARA TIMES DE DADOS - BASICS.

Além do postgres, será necessário a instalação da biblioteca `psycopg2` para que o python consiga se conectar ao banco.

[Documentação Oficial](https://www.psycopg.org/docs/)

## Bases de dados

### Northwind

Esta é uma versão do banco de dados de exemplo Northwind do Microsoft Access 2000, recriada para o SQLite3.

O banco de dados de exemplo Northwind foi fornecido com o Microsoft Access como um esquema de tutorial para gerenciar clientes, pedidos, estoque, compras, fornecedores, envio e funcionários de pequenas empresas. 

Northwind é um excelente esquema de tutorial para um ERP de pequenas empresas, com clientes, pedidos, estoque, compras, fornecedores, envio, funcionários e contabilidade de entrada única.

![Schema](./databases/northwind-er-diagram.png)

### Sqlite3 Version

DB dentro do diretório `databases` com o nome `northwind.db`. 

Não é necessário criar tabelas, pois o banco já está populado.

### Postgres Version

[Postgres Yugabyte Docs](https://docs.yugabyte.com/preview/sample-data/northwind/)

Etapas:

1. Subir uma instância do Postgres com Docker

```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
```

2. Dentro do Dbeaver, criar uma conexão com o Postgres
3. Executar o script `northwind-postgres-ddl` dentro do Dbeaver, criando as tabelas com seus respectivos schemas e relacionamentos
4. Executar o script `northwind-postgres-data.sql` dentro do Dbeaver, populando as tabelas com dados

