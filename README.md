# Mini Rede Social

## Autor: Michael Douglas P Lima
## Contato: michaelsjmvr@hotmail.com
## LinkedIn: [michael-douglas-640a11180](https://www.linkedin.com/in/michael-douglas-640a11180/)

## Descrição do Projeto
A Mini Rede Social é um projeto de uma rede social simplificada criada usando Python com a biblioteca PySide6 para a interface gráfica e SQLite3 para armazenamento de dados. O projeto permite que os usuários se registrem, façam login, postem mensagens, desloguem e vejam o feed de postagens.

## Pré-requisitos
Certifique-se de ter o Python instalado em seu sistema. Além disso, você precisará instalar a biblioteca PySide6, que pode ser instalada usando o pip:

## pip install PySide6


## Funcionalidades
- **Registro de Usuário:**
  - Os usuários podem se registrar inserindo um nome de usuário único e uma senha.
  - O sistema verifica se o nome de usuário já existe antes de permitir o registro.

- **Login de Usuário:**
  - Os usuários podem fazer login com seu nome de usuário e senha.
  - O sistema verifica as credenciais fornecidas e permite o acesso se forem válidas.

- **Postagem de Mensagens:**
  - Os usuários logados podem postar mensagens no feed.
  - O sistema verifica se o usuário está logado antes de permitir a postagem.

- **Feed de Postagens:**
  - O feed de postagens exibe as mensagens postadas por todos os usuários.
  - As postagens são exibidas no formato "nome do usuário: conteúdo da postagem".

- **Deslogar:**
  - Os usuários logados podem se deslogar para encerrar sua sessão.

## Estrutura do Projeto
O projeto está estruturado em uma única classe chamada MiniRedeSocial. A classe principal contém os seguintes métodos principais:

- criar_tabela_usuarios: Cria a tabela de usuários no banco de dados SQLite3.
- criar_tabela_postagens: Cria a tabela de postagens no banco de dados SQLite3.
- registrar_usuario: Registra um novo usuário após a validação dos campos de entrada.
- login_usuario: Realiza o login do usuário após a verificação das credenciais.
- postar_mensagem: Permite que os usuários logados postem mensagens no feed.
- atualizar_feed: Atualiza o feed de postagens com todas as mensagens postadas.
- mostrar_mensagem: Exibe mensagens informativas em uma caixa de diálogo.
- deslogar_usuario: Desloga o usuário da conta.

## Executando o Projeto
Para executar o projeto, siga estas etapas:

1. Clone ou faça o download do código-fonte do projeto.
2. Certifique-se de que o Python e as bibliotecas necessárias estejam instaladas.
3. Abra um terminal ou prompt de comando na pasta do projeto.
4. Execute o arquivo Python main.py:

## python main.py
Isso iniciará a aplicação da Mini Rede Social.

## Conclusão
A Mini Rede Social é um projeto Python simples que demonstra conceitos de programação de interfaces gráficas com o PySide6 e gerenciamento de bancos de dados SQLite3. Você pode expandir e aprimorar esse projeto adicionando recursos adicionais, como edição de postagens, curtidas, etc.
