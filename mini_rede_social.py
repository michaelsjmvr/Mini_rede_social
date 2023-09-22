# Importação das bibliotecas necessárias
import sys
import sqlite3
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QMessageBox

# Definição da classe principal para a Mini Rede Social
class MiniRedeSocial(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurações iniciais da janela principal
        self.setWindowTitle("Mini Rede Social")  # Define o título da janela
        self.setGeometry(100, 100, 600, 400)  # Define a posição e o tamanho da janela

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)  # Define o widget central

        layout = QVBoxLayout(central_widget)  # Cria um layout de grade vertical para organizar os elementos

        # Elementos da interface gráfica
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Nome de usuário")  # Placeholder para o campo de nome de usuário
        self.senha_input = QLineEdit(self)
        self.senha_input.setPlaceholderText("Senha")  # Placeholder para o campo de senha
        self.senha_input.setEchoMode(QLineEdit.Password)  # Configura o modo de eco para senha
        self.registrar_button = QPushButton("Registrar", self)
        self.registrar_button.clicked.connect(self.registrar_usuario)  # Conecta o botão ao método registrar_usuario

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText("Nome de usuário")  # Placeholder para o campo de nome de usuário no login
        self.senha_login_input = QLineEdit(self)
        self.senha_login_input.setPlaceholderText("Senha")  # Placeholder para o campo de senha no login
        self.senha_login_input.setEchoMode(QLineEdit.Password)  # Configura o modo de eco para senha no login
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login_usuario)  # Conecta o botão ao método login_usuario

        self.postagem_input = QLineEdit(self)
        self.postagem_input.setPlaceholderText("Digite sua postagem")  # Placeholder para o campo de postagem
        self.postar_button = QPushButton("Postar", self)
        self.postar_button.clicked.connect(self.postar_mensagem)  # Conecta o botão ao método postar_mensagem

        self.deslogar_button = QPushButton("Deslogar", self)
        self.deslogar_button.clicked.connect(self.deslogar_usuario)  # Conecta o botão ao método deslogar_usuario

        self.feed_list = QListWidget(self)  # Lista de postagens

        # Adiciona os elementos ao layout vertical
        layout.addWidget(self.nome_input)
        layout.addWidget(self.senha_input)
        layout.addWidget(self.registrar_button)
        layout.addWidget(self.login_input)
        layout.addWidget(self.senha_login_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.postagem_input)
        layout.addWidget(self.postar_button)
        layout.addWidget(self.feed_list)
        layout.addWidget(self.deslogar_button)

        # Conexão com o banco de dados SQLite3
        self.conexao = sqlite3.connect("minirede.db")
        self.criar_tabela_usuarios()
        self.criar_tabela_postagens()

        self.usuario_logado = None

    # Método para criar a tabela de usuários no banco de dados
    def criar_tabela_usuarios(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome_usuario TEXT UNIQUE,
                senha TEXT
            )
        ''')
        self.conexao.commit()

    # Método para criar a tabela de postagens no banco de dados
    def criar_tabela_postagens(self):
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS postagens (
                id INTEGER PRIMARY KEY,
                autor_id INTEGER,
                conteudo TEXT,
                FOREIGN KEY (autor_id) REFERENCES usuarios (id)
            )
        ''')
        self.conexao.commit()

    # Método para registrar um novo usuário
    def registrar_usuario(self):
        nome_usuario = self.nome_input.text()
        senha = self.senha_input.text()
        if nome_usuario and senha:
            cursor = self.conexao.cursor()

            # Verifique se o nome de usuário já existe no banco de dados
            cursor.execute("SELECT id FROM usuarios WHERE nome_usuario = ?", (nome_usuario,))
            resultado = cursor.fetchone()
            if resultado:
                self.mostrar_mensagem("Erro", "Nome de usuário já existe. Escolha outro.")
            else:
                cursor.execute("INSERT INTO usuarios (nome_usuario, senha) VALUES (?, ?)", (nome_usuario, senha))
                self.conexao.commit()
                self.mostrar_mensagem("Sucesso", "Usuário registrado com sucesso.")
                self.nome_input.clear()
                self.senha_input.clear()
        else:
            self.mostrar_mensagem("Erro", "Preencha todos os campos.")

    # Método para realizar o login do usuário
    def login_usuario(self):
        nome_usuario = self.login_input.text()
        senha = self.senha_login_input.text()
        if nome_usuario and senha:
            cursor = self.conexao.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE nome_usuario = ? AND senha = ?", (nome_usuario, senha))
            resultado = cursor.fetchone()
            if resultado:
                self.usuario_logado = resultado[0]
                self.mostrar_mensagem("Sucesso", "Login bem-sucedido.")
                self.atualizar_feed()
            else:
                self.mostrar_mensagem("Erro", "Nome de usuário ou senha incorretos.")
        else:
            self.mostrar_mensagem("Erro", "Preencha todos os campos.")

    # Método para postar uma nova mensagem
    def postar_mensagem(self):
        conteudo = self.postagem_input.text()
        
        # Verifique se o usuário está logado
        if not self.usuario_logado:
            self.mostrar_mensagem("Erro", "Você precisa fazer login para postar.")
            return
        
        if conteudo:
            cursor = self.conexao.cursor()
            cursor.execute("INSERT INTO postagens (autor_id, conteudo) VALUES (?, ?)", (self.usuario_logado, conteudo))
            self.conexao.commit()
            self.postagem_input.clear()
            self.atualizar_feed()
        else:
            self.mostrar_mensagem("Erro", "Digite uma postagem antes de postar.")

    # Método para atualizar o feed de postagens
    def atualizar_feed(self):
        self.feed_list.clear()
        cursor = self.conexao.cursor()
        cursor.execute("SELECT usuarios.nome_usuario, postagens.conteudo FROM postagens INNER JOIN usuarios ON postagens.autor_id = usuarios.id")
        for row in cursor.fetchall():
            postagem = f"{row[0]}: {row[1]}"
            self.feed_list.addItem(postagem)

    # Método para exibir uma mensagem em uma caixa de diálogo
    def mostrar_mensagem(self, titulo, mensagem):
        mensagem_box = QMessageBox(self)
        mensagem_box.setWindowTitle(titulo)
        mensagem_box.setText(mensagem)
        mensagem_box.setStandardButtons(QMessageBox.Ok)
        mensagem_box.exec()

    # Método para deslogar o usuário
    def deslogar_usuario(self):
        self.usuario_logado = None
        self.login_input.clear()
        self.senha_login_input.clear()
        self.feed_list.clear()
        self.mostrar_mensagem("Sucesso", "Usuário deslogado com sucesso.")

# Função principal
if __name__ == "__main__":
    app = QApplication(sys.argv)
    rede_social = MiniRedeSocial()
    rede_social.show()
    sys.exit(app.exec())
