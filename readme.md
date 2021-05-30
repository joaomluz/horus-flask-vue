# Horus teste de programação

Aplicação de exemplo contendo Backend em Flask e Frontend em Vue e ainda um banco de dados SQL.   
Objetivo geral: Criar uma pequena aplicação para que um usuário possa gerenciar uma lista de contatos.

**Table of Contents**
* [Before start](#before-start)
* [Requirements](#requirements)
* [Installation](#installation)
* [Backend](#backend)
    * [Queries and Routes](#queries-and-routes)
    * [Starting up backend](#starting-up-backend)
    * [Testing backend](#testing-backend)
* [Frontend](#frontend)
    * [Starting up frontend](#starting-up-frontend)
    * [Creating new contact](#creating-new-contact)
    * [Updating contact](#updating-contact)
    * [Removing contact](#removing-contact)
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
Quando for solicitado para escolher a isntalação do Vue, selecione os defaults para Vue 2 e aparte ENTER

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

### Queries and Routes
O endereço utilizado do servidor para essa documentação será 127.0.0.1, mas para efeitos de demonstração o servidor escuta no "0.0.0.0", então se seu linux tiver conectado à um roteador você poderá acessar o servidor de fora em um endereço local.   

As respostas serão dadas em JSON.   
- Listando os contatos
    - [GET] http://127.0.0.1/
    - [JSON] {["id": 1, "contact_name": "nome", "contact_phone": "+55119000080000"], ...}
- Adicionando um novo contato
    - [POST] http://127.0.0.1/new/?contact_name=nome&contact_phone=+55119000080000
    - [JSON] {"status": 1} 
    - [JSON-ERR] {"status": 0, "error": "SQL error | Phone exists"}
- Alterando um telefone
    - [GET] http://127.0.0.1/update/1?method=update&contact_phone=+15962547896
    - [JSON] {"status": 1}
    - [JSON-ERR] {"status": 0, "error": "SQL error | Phone exists | Not found"} 
- Removendo um contato
    - [GET] http://127.0.0.1/update/1?method=delete
    - [JSON] {"status": 1} 
    - [JSON-ERR] {"status": 0, "error": "SQL error | Phone exists | Not found"} 

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

## Frontend
O frontend ainda está sendo finalizado para que contemple todas as operações de CRUD as quais o backend é capaz de lidar, mas ele já possui uma interface amigável e é capaz de adicionar novos contatos e listar os contatos inseridos no banco.   

Segue a tela principal, onde é listado os contatos:   
![list-page](/img/contacts-list.PNG)

Obs. A Documentação nessa seção não está concluida, para maiores informações navegue nas pastas e arquivos de client\src, todos eles integram esse projeto

### Starting up frontend
Para iniciar o frontend foi criado um script, run-fron-end.sh, dessa forma basta entrar na pasta do projeto e executar:   
```bash
$ ./run-fron-end.sh 
```
Obs. O frontend irá iniciar em modo de desenvolvimento, pois ainda não existe uma certificação de que tudo esteja funcionando corretamente e livre de bugs. 

### Creating new contact
A criação de um novo contato a partir do backend é feita através do botão "Novo contato", localizado na perte superior esquerda.  

Essa requisição é feita para o backend seguindo a [documentação](#queries-and-routes).   

Deve se preencher os campos:
- Nome, com o nome do novo contato
- Telefone, com o telefone desse contato

Segue exemplo do modal que irá aparecer:
![new-contact-modal](/img/add-new-contact-modal.PNG)

### Updating contact
Para atualizar um contato, clique em "Update" ao lado do contato que deseja atualizar, altere o número de telefone e clique no botão "Atualizar".   

Se tudo ocorrer como planejado, a mensagem "Contato atualizado" deve aparecer na tela.   

### Removing contact
Para remover um contato, basta clicar no botão "Delete" ao lado do contato, a mensagem "Contato removido" confirma a remoção.   
[ATENÇÃO] Não existe confirmação para a remoção do contato.   