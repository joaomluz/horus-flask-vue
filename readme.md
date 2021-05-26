# Horus teste de programação

Aplicação de exemplo contendo Backend em Flask e Frontend em Vue e ainda um banco de dados SQL.   
Objetivo geral: Criar uma pequena aplicação para que um usuário possa gerenciar uma lista de contatos.

**Table of Contents**
* [Before start](#before-start)
* [Requirements](#requirements)
* [Installation](#installation)
* [Backend](#backend)
    * [Queries & Routes](#queries-n-routes)
    * [Starting up backend](#starting-up-backend)
    * [Testing backend](#testing-backend)
## Before start
Foi desenvolvido alguns scripts para facilitar a instalção e operação, mas é possível executar õs comandos de maneira manual   

## Requirements
Para utilizar esse projeto, você vai precisar de:
- Linux OS (Debian ou Ubuntu)
- python3.8+
- python3-pip
- python3-venv
- nodejs 10+
- npm

Aplicativos e demais dependências serão instaladas automaticamente ao chamar o script install-dependencies.sh   
Obs. Para fazer a instalação de pacotes adicionais você vai precisar de acesso root

## Installation
- Faça um clone do repositório em uma pasta que voc6e possua acesso completo (leitura/escrita/execução)
- No Shell execute:
```bash
$ chmod +x install-*
$ sudo ./install-dependencies.sh /path/to/install
```
Obs. Substitua /path/to/install pelo caminho absoluto desejado para instalação da aplicação. Se omitido a aplicação será instalada em /opt/BrunoNatali/   
   
Assim que o sistema estiver pronto para receber os pacotes das stacks mencionadas execute no Shell:
```bash 
$ ./install-apps.sh
```

## Backend
O Backend foi escrito em FLask, Flask é um pequeno framework web escrito em Python.   
Sua estrutura de pastas é demonstrada a seguir:
```shell
+-- database
|   +-- schema.sql  # Estrutura do banco de dados
+-- project
|   +-- __init__.py
|   +-- models.py   # Estrutura de manipulação do banco
|   +-- server.py   # Aplicação principal, API de interface
+-- test
|   +-- __init__.py
|   +-- server_test.py
+-- create_db.py    # Script básico para criação inicial do banco
```

### Queries & Routes
O endereço utilizado do servidor para essa documentação será 127.0.0.1, mas para efeitos de demonstração o servidor escuta no "0.0.0.0", então se seu linux tiver conectado à um roteador você poderá acessar o servidor de fora em um endereço local.   
- Listando os contatos
    - [GET] http://127.0.0.1/
    - [JSON] ```json {["id": 1, "contact_name": "nome", "contact_phone": "+55119000080000"], ...}```
- Adicionando um novo contato
    - [POST] http://127.0.0.1/new/?contact_name=nome&contact_phone=+55119000080000
    - [JSON] ```json {"status": 1} ```
    - [JSON-ERR] ```json {"status": 0, "error": "SQL error | Phone exists"} ```
- Alterando um telefone
    - [GET] http://127.0.0.1/update/1?method=update&contact_phone=+15962547896
    - [JSON] ```json {"status": 1} ```
    - [JSON-ERR] ```json {"status": 0, "error": "SQL error | Phone exists | Not found"} ```
- Removendo um contato
    - [GET] http://127.0.0.1/update/1?method=delete
    - [JSON] ```json {"status": 1} ```
    - [JSON-ERR] ```json {"status": 0, "error": "SQL error | Phone exists | Not found"} ```

Obs. Se alguma query ou path URL não for cumprido, um HTTP 400 será retornado.

### Starting up backend
Para iniciar o Backend apenas rode o script 'run-back-end.sh':
```bash 
$ cd /path/to/install && ./run-back-end.sh
```
Lembrando de trocar "/path/to/install" pelo local escolhido para instalação da aplicação   
Ou você pode executar ele manualmente da seguinte forma:
```bash 
$ cd /path/to/install/backend && FLASK_APP=project/server.py python -m flask run --host=0.0.0.0
```

### Testing backend
O teste unitário do backend é feito utilizando a ferramenta [pytest](https://pytest.org). Mesmo numa aplicação tão pequena de demonstração, algumas dezenas de testes podem ser executados, mas como o objetivo dessa parte, para esse projeto, é garantir o funcionamento mínimo e a execução de testes unitários, são feitos 4 testes que incluiem validação das rotas e comunicação com o banco de dados.   
Para executar o teste:
```bash 
$ cd /path/to/install/backend
$ source env/bin/activate
$ python -m pytest
```