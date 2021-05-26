# Horus teste de programação

Aplicação de exemplo contendo Backend em Flask e Frontend em Vue e ainda um banco de dados SQL

**Table of Contents**
* [Before start](#before-start)
* [Requirements](#requirements)
* [Installation](#installation)
* [Backend](#backend)
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
$ sudo ./install-dependencies.sh /path/to/install/dir
```
Obs. Substitua /path/to/install/dir pelo caminho absoluto desejado para instalação da aplicação. Se omitido a aplicação será instalada em /opt/BrunoNatali/   
   
Assim que o sistema estiver pronto para receber os pacotes das stacks mencionadas execute no Shell:
```bash 
$ ./install-apps.sh
```

## Backend
O Backend foi escrito em FLask, Flask é um pequeno framework web escrito em Python.   
Sua estrutura de pastas é demonstrada a seguir:
```shell
+-- database
|   +-- schema.sql
+-- project
|   +-- __init__.py
|   +-- models.py
|   +-- server.py
+-- test
|   +-- __init__.py
|   +-- server_test.py
+-- create_db.py
```

### Starting up backend
Para iniciar o Backend apenas rode o script 'run-back-end.sh':
```bash 
$ cd /path/to/install/dir && ./run-back-end.sh
```
Lembrando de trocar "/path/to/install/dir" pelo local escolhido para instalação da aplicação   
Ou você pode executar ele manualmente da seguinte forma:
```bash 
$ cd /path/to/install/dir/backend && FLASK_APP=project/server.py python -m flask run --host=0.0.0.0
```

### Testing backend
O teste unitário do backend é feito utilizando a ferramenta [pytest](https://pytest.org). Mesmo numa aplicação tão pequena de demonstração, algumas dezenas de testes podem ser executados, mas como o objetivo dessa parte, para esse projeto, é garantir o funcionamento mínimo e a execução de testes unitários, são feitos 4 testes que incluiem validação das rotas e comunicação com o banco de dados.   
Para executar o teste:
```bash 
$ cd /path/to/install/dir/backend
$ source env/bin/activate
$ python -m pytest
```