import os
import typing
import mysql.connector as mysql
import numpy as np
import json
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel, QListWidgetItem
from PyQt5.QtCore import QCoreApplication, pyqtSignal

from tela_login import TelaLogin
from tela_cadastrar import TelaCadastrar
from tela_inicial import TelaInicial
from tela_jogo import TelaJogo
from tela_perfil import TelaPerfil
from tela_review import TelaReview
from admin import TelaADM
from tela_login_adm import TelaLoginADM
from tela_apagar_jogo import TelaApagarJogo
from cliente import Cliente

class MainMultitelas(QtWidgets.QWidget):
    """
    Classe principal que controla a aplicação.

    ...

    Methods
    -------
    setupUi(Main: QtWidgets.QMainWindow):
        Configura a interface do usuário para a janela principal.

    """

    def setupUi(self, Main):
        """
        Configura a interface do usuário para a janela principal.

        O método setupUi é responsável por configurar a interface do usuário para a janela principal.

        Parameters
        ----------
        Main (QtWidgets.QMainWindow)
            O objeto da janela principal.
        """

        Main.setObjectName('Main')
        Main.resize(640, 480)

        jogo_id = 1
        self.jogoClicado = pyqtSignal(int)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
      
        self.tela_login = TelaLogin()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastrar =  TelaCadastrar()
        self.tela_cadastrar.setupUi(self.stack1)

        self.tela_inicial = TelaInicial()
        self.tela_inicial.setupUi(self.stack2)

        self.tela_jogo = TelaJogo(jogo_id)
        self.tela_jogo.setupUi(self.stack3)

        self.tela_perfil = TelaPerfil()
        self.tela_perfil.setupUi(self.stack4)

        self.tela_login_adm = TelaLoginADM()
        self.tela_login_adm.setupUi(self.stack5)

        self.tela_adm = TelaADM()
        self.tela_adm.setupUi(self.stack6)

        self.tela_apagar_jogo = TelaApagarJogo()
        self.tela_apagar_jogo.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        

class Main(QMainWindow, MainMultitelas):
    """
    Classe principal do aplicativo que herda da classe MainMultitelas e QMainWindow.
    Esta classe representa a janela principal do aplicativo.

    ...

    Attributes
    ----------
    jogo_selecionado_id : int 
        O ID do jogo selecionado
    usuario_logado : None
        O usuário logado no momento. Inicialmente, nenhum usuário está logado.
    cliente : Cliente
        Uma instância da classe Cliente.

    Methods
    -------
    __init__(self, parent=None)
        Construtor da classe. Inicializa a janela e configura as conexões dos sinais e slots.

    botao_cadastrar(self)
        Função chamada quando o botão de cadastro é clicado. Realiza o cadastro de um novo usuário.

    login(self)
        Função chamada quando o botão de login é clicado. Realiza o login do usuário.
    
    exibirJogos(self, jogos)
        Exibe a lista de jogos na interface gráfica.

    itemClicado(self, item: QListWidgetItem)
        Lida com o evento de clique em um item da lista de jogos.

    abrirTelaJogo(self, jogo_id)
        Abre a tela de um jogo específico.

    carregarInformacoes(self, jogo_id)
        Carrega as informações de um jogo específico.

    abrirTelaReview(self, username)
        Abre a tela para escrever uma review de um jogo.

    exibir_reviews(self, jogo_id)
        Exibe as reviews de um jogo específico.

    abrirPerfilUsuario(self)
        Abre a tela do perfil do usuário logado.

    exibirReviewsUsuarios(self, usuario_id, num_reviews)
        Exibe as últimas reviews de um usuário específico.

    abrirTelaADM(self)
        Abre a tela de login do administrador.

    adicionarJogoADM(self)
        Adiciona um jogo na lista de jogos cadastrados.

    carregarJogosADM(self):
        Carrega os jogos cadastrados.

    def itemClicadoADM(self, item: QListWidgetItem):
        Lida com o evento de clique em um item da lista de jogos.
    
    def pesquisarJogos(self):
        Pesquisa os jogos de acordo com os filtros selecionados.

    def pesquisarJogosADM(self):
        Pesquisa os jogos pelo nome.
        
    botao_voltar(self):
        Função chamada quando o botão de voltar é clicado.

    botao_deslogar(self):
        Função chamada quando o botão de deslogar é clicado.

    abrirTelaCadastrar(self):
        Abre a tela de cadastro de novos usuários.

    abrir_tela_inicial(self):
        Retorna para a tela inicial.

    abrirTelaLoginADM(self):
        Abre a tela de login do administrador.

    voltarTelaADM(self):
        Volta para a tela do administrador.

    abrirJogos(self):
        Abre a tela de jogos.
    """

    def __init__(self, parent=None):
        """
        Parameters
        ----------
        parent : NoneType
            Widget pai da janela. Por padrão, é None.
        """

        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.jogo_selecionado_id = None
        self.usuario_logado = None
        self.username = None
        self.cliente = Cliente()

        self.tela_login.pushButton.clicked.connect(self.login)
        self.tela_login.pushButton_2.clicked.connect(self.abrirTelaCadastrar)
        self.tela_login.pushButton_4.clicked.connect(self.abrirTelaLoginADM)

        self.tela_cadastrar.pushButton.clicked.connect(self.botao_cadastrar)
        self.tela_cadastrar.pushButton_2.clicked.connect(self.botao_voltar)

        self.tela_inicial.pushButton.clicked.connect(self.abrirPerfilUsuario)
        self.tela_inicial.pushButton_2.clicked.connect(self.botao_deslogar)
        self.tela_inicial.pushButton_3.clicked.connect(self.pesquisarJogos)
        self.tela_inicial.jogoSelecionado.connect(self.abrirTelaJogo)

        self.tela_perfil.sairButton.clicked.connect(self.botao_deslogar)
        self.tela_perfil.paginaInicialButton.clicked.connect(self.abrir_tela_inicial)

        self.tela_login_adm.pushButton.clicked.connect(self.abrirTelaADM)
        self.tela_login_adm.pushButton_3.clicked.connect(self.botao_deslogar)

        self.tela_adm.pushButton.clicked.connect(self.adicionarJogoADM)
        self.tela_adm.pushButton_3.clicked.connect(self.botao_deslogar)
        self.tela_adm.pushButton_2.clicked.connect(self.abrirJogos)

        self.tela_apagar_jogo.pushButton.clicked.connect(self.voltarTelaADM)
        self.tela_apagar_jogo.pushButton_2.clicked.connect(self.pesquisarJogosADM)

    def botao_cadastrar(self):
        """
        Função chamada quando o botão de cadastro é clicado. Realiza o cadastro de um novo usuário.

        Esse método é chamado quando o botão de cadastro é pressionado. Ele obtém os valores inseridos nos campos
        de texto da tela de cadastro e envia uma mensagem para o servidor com essas informações. Caso o cadastro 
        seja realizado com sucesso, exibe uma mensagem informativa. Caso contrário, exibe uma mensagem de aviso.
        """

        self.username = self.tela_cadastrar.lineEdit.text()
        senha = self.tela_cadastrar.lineEdit_3.text()
        email = self.tela_cadastrar.lineEdit_2.text()
        data_criacao = datetime.date.today().strftime('%Y-%m-%d')

        if not (self.username == '' or email == '' or senha == '' or data_criacao == ''):
            msg = '1' + '-' + self.username + '-' + email + '-' + senha + '-' + data_criacao
            recebeu = self.cliente.enviar(msg)
            if recebeu == '1':
                        QMessageBox.information(self, 'Cadastro Concluído', 'Cadastro realizado com sucesso!')
                        self.tela_cadastrar.lineEdit.setText('')
                        self.tela_cadastrar.lineEdit_2.setText('')
                        self.tela_cadastrar.lineEdit_3.setText('')
            else:
                        QMessageBox.warning(self, 'Usuário Existente', 'Usuário já existe!')
        else:
            QMessageBox.warning(self, 'Cadastro de Usuários', 'Todos os valores devem ser preenchidos.')
        self.tela_cadastrar.lineEdit.clear()
        self.tela_cadastrar.lineEdit_2.clear()
        self.tela_cadastrar.lineEdit_3.clear()

    def login(self):
        """
        Função chamada quando o botão de login é clicado. Realiza o login do usuário.

        Esse método é chamado quando o botão de login é pressionado. Ele obtém o nome de usuário e a senha 
        inseridos nos campos de texto da tela de login e envia uma mensagem para o servidor com essas informações. 
        Caso o login seja bem-sucedido, exibe a tela inicial com os jogos disponíveis para o usuário. Caso contrário,
        exibe uma mensagem de erro.
        """

        self.username = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()

        mensagem = '0' + '-' + self.username + '-' + senha
        resposta = self.cliente.enviar(mensagem)
        if resposta != '0':
            self.cliente.enviar('8-' + self.username) 
            self.usuario_id = self.cliente.enviar('9-' + self.username)

            mensagem_jogos = '4'
            resposta_jogos = self.cliente.enviar(mensagem_jogos)
            jogos = resposta_jogos.split('\n')
            self.exibirJogos(jogos)
            self.pesquisarJogos()

            self.QtStack.setCurrentIndex(2)
            self.tela_login.lineEdit.clear()
            self.tela_login.lineEdit_2.clear()
        else:
            QMessageBox.critical(self, 'Erro', 'Usuário ou senha incorretos.')
    
    def exibirJogos(self, jogos):
        """
        Exibe a lista de jogos na interface gráfica.

        Essa função exibe a lista de jogos na interface gráfica. Ela recebe uma lista
        de jogos e exibe cada jogo na lista de forma apropriada.

        Parameters
        ----------
        jogos : list
            A lista de jogos a ser exibida.
        """

        self.tela_inicial.listWidget.clear()
        if jogos:
            for jogo in jogos:
                item = QListWidgetItem()
                jogo_data = jogo.split(' | ')
                if len(jogo_data) >= 2:
                    jogo_id = int(jogo_data[0])
                    name_year = jogo_data[1].split(' (')
                    if len(name_year) >= 2:
                        name, year = name_year[0], name_year[1][:-1]
                        item.setText(f"{name} ({year})")
                    else:
                        item.setText(jogo_data[1])
                    item.setData(QtCore.Qt.UserRole, jogo_id)
                    self.tela_inicial.listWidget.addItem(item)
                else:
                    print(f"Invalid format for jogo: {jogo}")
            
            self.tela_inicial.listWidget.itemClicked.connect(self.itemClicado)

        else:
            item = QListWidgetItem("Nenhum jogo encontrado")
            self.tela_inicial.listWidget.addItem(item)

    def itemClicado(self, item: QListWidgetItem):
            """
            Lida com o evento de clique em um item da lista de jogos.

            Essa função é chamada quando um item da lista de jogos é clicado. Ela emite um sinal
            contendo o ID do jogo selecionado.

            Parameters
            ----------
            item : QListWidgetItem
                O item da lista de jogos clicado.
            """

            jogo_id = item.data(QtCore.Qt.UserRole)
            self.tela_inicial.jogoSelecionado.emit(jogo_id)

    def abrirTelaJogo(self, jogo_id):
        """
        Abre a tela de um jogo específico.

        Esse método é chamado quando um jogo é selecionado na tela inicial. Ele recebe o ID do 
        jogo selecionado como argumento e envia uma mensagem para o servidor solicitando o nome do jogo 
        correspondente ao ID. Em seguida, exibe a tela do jogo, carrega as informações do jogo e exibe as 
        reviews relacionadas a ele.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo a ser aberto.
        """

        mensagem = '2-' + str(jogo_id)
        resposta = self.cliente.enviar(mensagem) 

        if jogo_id != 0:
            self.tela_jogo = TelaJogo(jogo_id)
            self.tela_jogo.setupUi(self.stack3)
            
            self.tela_jogo.voltarButton.clicked.connect(self.abrir_tela_inicial)
            self.tela_jogo.sairButton.clicked.connect(self.botao_deslogar)
            self.tela_jogo.reviewButton.clicked.connect(self.abrirTelaReview)
            self.tela_jogo.perfilButton.clicked.connect(self.abrirPerfilUsuario)

            nome_jogo = resposta

            self.stack2.setWindowTitle(nome_jogo)
            self.QtStack.setCurrentIndex(3)
            self.carregarInformacoes(jogo_id)
            self.tela_jogo.reviewsList.scrollToBottom()
            self.exibir_reviews(jogo_id)
        else:
            QMessageBox.warning(self, 'Jogo não encontrado', 'O jogo selecionado não foi encontrado!')

    def carregarInformacoes(self, jogo_id):
        """
        Carrega as informações de um jogo específico.

        Esse método é responsável por obter as informações de um jogo a partir do seu ID. 
        Ele envia uma mensagem para o servidor solicitando as informações do jogo com o ID especificado. 
        Caso as informações sejam recebidas com sucesso, elas são exibidas na tela do jogo.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo do qual as informações serão carregadas.
        """

        mensagem = '6-' + str(jogo_id)
        resposta = self.cliente.enviar(mensagem)

        if resposta:
            carregar_informacoes = json.loads(resposta)
            nome = carregar_informacoes['nome']
            desenvolvedor = carregar_informacoes['desenvolvedor']
            distribuidora = carregar_informacoes['distribuidora']
            ano_lancamento = carregar_informacoes['ano_lancamento']
            descricao = carregar_informacoes['descricao']

            self.tela_jogo.label.setText(f"{nome} - {ano_lancamento}")
            self.tela_jogo.label.setFont(QtGui.QFont("Arial", 20))
            self.tela_jogo.infoLabel.setText(f"Desenvolvedor: {desenvolvedor}\nDistribuidora: {distribuidora}\nDescrição: {descricao}")
        else:
            self.tela_jogo.label.setText("Jogo não encontrado")
            self.tela_jogo.infoLabel.setText("")

    def abrirTelaReview(self):
        """
        Abre a tela para escrever uma review de um jogo.

        Esse método é chamado quando o botão de adicionar review é pressionado na tela do jogo. 
        Ele exibe uma caixa de diálogo para o usuário digitar sua review. Quando o usuário confirma a review, 
        ela é enviada para o servidor junto com o ID do usuário e do jogo correspondentes. Em caso de sucesso, 
        uma mensagem informativa é exibida e as reviews são atualizadas.

        Parameters
        ----------
        username : str
            O nome de usuário do autor da review.
        """

        review, ok = QtWidgets.QInputDialog.getText(self.stack3, "Escrever Review", "Digite sua review:")
        if ok:
            jogo_id = self.tela_jogo.jogo_id
            usuario_id = self.cliente.enviar('9-' + self.username)
            mensagem = f"3-{usuario_id}-{jogo_id}-{review}"
            resposta = self.cliente.enviar(mensagem)
            if resposta == '1':
                QMessageBox.information(self.stack3, "Review Salva", "A sua review foi salva com sucesso!")
                self.exibir_reviews(jogo_id)
            else:
                QMessageBox.critical(self.stack3, "Erro", "Ocorreu um erro ao salvar a review.")
    

    def exibir_reviews(self, jogo_id):
        """
        Exibe as reviews de um jogo específico.

        Esse método é responsável por exibir as reviews de um jogo na tela do jogo. Ele envia 
        uma mensagem para o servidor solicitando as reviews do jogo com o ID especificado. Caso as reviews 
        sejam recebidas com sucesso, elas são exibidas na lista de reviews da tela do jogo.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo do qual as reviews serão exibidas.
        """

        mensagem = f"5-{str(jogo_id)}" 
        resposta = self.cliente.enviar(mensagem)

        if resposta != 0:
            reviews = resposta.split('\n')
            self.tela_jogo.reviewsList.clear()

            for review in reviews:
                review_items = review.split(' | ')
                item = QtWidgets.QListWidgetItem(review)
                self.tela_jogo.reviewsList.addItem(item)

            self.tela_jogo.reviewsList.setCurrentRow(self.tela_jogo.reviewsList.count() - 1)
        else:
            self.tela_jogo.reviewsList.clear()
            QMessageBox.warning(self, 'Erro ao obter reviews', 'Ocorreu um erro ao obter as reviews do jogo.')

    def abrirPerfilUsuario(self):
        """
        Abre a tela do perfil do usuário logado.

        Esse método é chamado quando o botão de perfil do usuário é pressionado na tela 
        do jogo. Ele exibe a tela de perfil do usuário.
        """

        self.QtStack.setCurrentIndex(4)
        usuario_id = self.cliente.enviar('9-' + self.username)
        self.tela_perfil.usernameLabel.setText(self.username)
        self.exibirReviewsUsuarios(usuario_id, 50)

    def exibirReviewsUsuarios(self, usuario_id, num_reviews):
        """
        Exibe as últimas reviews de um usuário específico.

        Esse método é responsável por exibir as últimas reviews de um usuário específico. Ao ser chamado,
        o método envia uma mensagem ao cliente para solicitar as reviews do usuário especificado. Em seguida,
        recebe a resposta do cliente. Se houver reviews para exibir, o método atualiza a lista de reviews na
        tela com as últimas reviews obtidas. Caso contrário, exibe uma mensagem de aviso informando que ocorreu
        um erro ao obter as últimas reviews do usuário.

        Parameters
        ----------
        usuario_id : int 
            O ID do usuário do qual as reviews serão exibidas.
        num_reviews : int
            O número máximo de reviews a serem exibidas.
        """

        mensagem = f"7-{usuario_id}-{num_reviews}"
        resposta = self.cliente.enviar(mensagem)
        if resposta != '0':
            ultimas_reviews = resposta.split('\n')
            self.tela_perfil.reviewsList.clear()
            for review in ultimas_reviews:
                review_items = review.split(' | ')
                item = QtWidgets.QListWidgetItem(review)
                self.tela_perfil.reviewsList.addItem(item)
        else:
            QMessageBox.warning(self, 'Erro ao obter reviews', 'Ocorreu um erro ao obter as últimas reviews do usuário.')

    def abrirTelaADM(self):
        """
        Abre a tela de login do administrador.

        Esse método é chamado quando o botão de login do administrador é pressionado na tela
        de login. Ele obtém o nome de usuário e a senha inseridos nos campos de texto da tela de login 
        do administrador e envia uma mensagem para o servidor com essas informações. Caso o login seja 
        bem-sucedido, exibe a tela do administrador. Caso contrário, exibe uma mensagem de erro.
        """

        username = self.tela_login_adm.lineEdit.text()
        senha = self.tela_login_adm.lineEdit_2.text()

        mensagem = '10' + '-' + username + '-' + senha
        resposta = self.cliente.enviar(mensagem)
        if resposta != '0':
            self.QtStack.setCurrentIndex(6)
        else:
            QMessageBox.warning(self, 'Erro ao logar', 'Usuário ou senha incorretos.')
        self.tela_login_adm.lineEdit.clear()
        self.tela_login_adm.lineEdit_2.clear()

    def adicionarJogoADM(self):
        """
        Adiciona um jogo na lista de jogos cadastrados.

        Esse método é chamado quando o botão de adicionar jogo é pressionado na tela do
        administrador. Ele obtém as informações do jogo inseridas nos campos de texto da tela de adição
        de jogos e envia uma mensagem para o servidor com essas informações. Caso o jogo seja adicionado
        com sucesso, exibe uma mensagem informativa. Caso contrário, exibe uma mensagem de erro.
        """

        nome = self.tela_adm.lineEdit.text()
        desenvolvedor = self.tela_adm.lineEdit_2.text()
        distribuidora = self.tela_adm.lineEdit_3.text()
        ano_lancamento = self.tela_adm.lineEdit_5.text()
        descricao = self.tela_adm.textEdit.toPlainText()

        mensagem = '11' + '-' + nome + '-' + desenvolvedor + '-' + distribuidora + '-' + ano_lancamento + '-' + descricao
        resposta = self.cliente.enviar(mensagem)
        if resposta != 0:
            QtWidgets.QMessageBox.information(None, "Sucesso", "Jogo adicionado com sucesso!")
            self.tela_adm.lineEdit.clear()
            self.tela_adm.lineEdit_2.clear()
            self.tela_adm.lineEdit_3.clear()
            self.tela_adm.lineEdit_5.clear()
            self.tela_adm.textEdit.clear()
        else:
            QtWidgets.QMessageBox.critical(None, "Erro", "Por favor, preencha todos os campos do jogo.")

    def carregarJogosADM(self):
        """
        Carrega os jogos cadastrados.

        Esse método é responsável por carregar os jogos cadastrados. Ao ser chamado, o método envia
        uma mensagem ao cliente para solicitar os jogos cadastrados. Em seguida, ele recebe a resposta
        do cliente. Se houver jogos cadastrados, o método percorre a lista de jogos e adiciona cada um deles
        a lista de jogos cadastrados. Caso contrário, se não houver resposta ou ocorrer algum
        erro, é exibida uma mensagem de erro alertando sobre a falha ao carregar os jogos cadastrados.
        """

        mensagem = '12'
        resposta = self.cliente.enviar(mensagem)
        
        if resposta:
            self.tela_apagar_jogo.listWidget.clear()
            jogos = resposta.split('\n')
            for jogo in jogos:
                item = QListWidgetItem()
                jogo_data = jogo.split(' | ')
                if len(jogo_data) >= 2:
                    jogo_id = int(jogo_data[0])
                    name_year = jogo_data[1].split(' (')
                    if len(name_year) >= 2:
                        name, year = name_year[0], name_year[1][:-1]
                        item.setText(f"{name} ({year})")
                    else:
                        item.setText(jogo)
                    item.setData(QtCore.Qt.UserRole, jogo_id)
                    self.tela_apagar_jogo.listWidget.addItem(item)
                else:
                    print(f"Invalid format for jogo: {jogo}")

            self.tela_apagar_jogo.listWidget.itemClicked.connect(self.itemClicadoADM)

    def itemClicadoADM(self, item: QListWidgetItem):
        """
        Lida com o evento de clique em um item da lista de jogos.

        Essa função é chamada quando um item da lista de jogos é clicado. Ela exibe um diálogo de confirmação
        para o usuário e, se confirmado, emite um sinal contendo o ID do jogo selecionado.

        Parameters
        ----------
        item : QListWidgetItem
            O item da lista de jogos clicado.
        """
        jogo_id = item.data(QtCore.Qt.UserRole)

        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setText("Deseja excluir o jogo selecionado?")
        confirm_dialog.setWindowTitle("Confirmação")
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        response = confirm_dialog.exec_()

        if response == QMessageBox.Yes:
            mensagem = f'13-{jogo_id}'
            resposta = self.cliente.enviar(mensagem)

            if resposta == "1":
                self.tela_apagar_jogo.listWidget.takeItem(self.tela_apagar_jogo.listWidget.row(item))
            else:
                error_dialog = QMessageBox()
                error_dialog.setIcon(QMessageBox.Warning)
                error_dialog.setText("Falha ao excluir o jogo.")
                error_dialog.setWindowTitle("Erro")
                error_dialog.exec_()

    def pesquisarJogos(self):
        """
        Pesquisa os jogos de acordo com os filtros selecionados.

        Essa função realiza a pesquisa de jogos com base nos filtros selecionados na combobox e no texto
        digitado no lineEdit. Ela emite um sinal com a lista de jogos resultante da pesquisa.
        """
        
        filtro = self.tela_inicial.comboBox.currentText()
        pesquisa = self.tela_inicial.lineEdit.text()

        mensagem = f'14-{filtro}-{pesquisa}'
        resposta = self.cliente.enviar(mensagem)

        if resposta:
            jogos = resposta.split('\n')
            if jogos:
                self.exibirJogos(jogos)
            else:
                QMessageBox.warning(self, "Nenhum jogo encontrado", "Não foram encontrados jogos correspondentes à pesquisa.")
                self.tela_inicial.listWidget.clear()
        else:
            self.tela_inicial.listWidget.clear()

    def pesquisarJogosADM(self):
        """
        Pesquisa os jogos pelo nome.

        Esta função é chamada quando o botão de pesquisa é clicado.
        Realiza a pesquisa dos jogos pelo nome digitado no lineEdit e exibe os resultados na listWidget.
        """
        nome_jogo = self.tela_apagar_jogo.lineEdit.text()

        mensagem = f'14-Nome-{nome_jogo}'
        resposta = self.cliente.enviar(mensagem)

        if resposta:
            jogos = resposta.split('\n')
            if jogos:
                self.tela_apagar_jogo.listWidget.clear()
                for jogo in jogos:
                    item = QListWidgetItem()
                    jogo_data = jogo.split(' | ')
                    if len(jogo_data) >= 2:
                        jogo_id = int(jogo_data[0])
                        name_year = jogo_data[1].split(' (')
                        if len(name_year) >= 2:
                            name, year = name_year[0], name_year[1][:-1]
                            item.setText(f"{name} ({year})")
                        else:
                            item.setText(jogo)
                        item.setData(QtCore.Qt.UserRole, jogo_id)
                        self.tela_apagar_jogo.listWidget.addItem(item)
                    else:
                        print(f"Invalid format for jogo: {jogo}")
            else:
                self.tela_apagar_jogo.listWidget.clear()
                self.tela_apagar_jogo.listWidget.addItem("Nenhum jogo encontrado")
        else:
            self.listWidget.clear()

    def botao_voltar(self):
        """
        Função chamada quando o botão de voltar é clicado.

        Esse método é chamado quando o botão de voltar é clicado na interface. Esse método contém a
        lógica para retornar à tela anterior.
        """

        self.QtStack.setCurrentIndex(0)

    def botao_deslogar(self):
        """
        Função chamada quando o botão de deslogar é clicado.

        Esse método é chamado quando o botão de deslogar é clicado na interface. Essa linha de código
        faz com que a interface retorne à tela de login.
        """

        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastrar(self):
        """
        Abre a tela de cadastro de novos usuários.

        Esse método é responsável por abrir a tela de cadastro de novos usuários.
        Ao ser chamado, abre a tela de cadastro de usuários. Essa linha de código faz com que a interface
        mude para a tela de cadastro, permitindo que novos usuários se registrem no sistema.
        """

        self.QtStack.setCurrentIndex(1)

    def abrir_tela_inicial(self):
        """
        Retorna para a tela inicial.

        Esse método é responsável por retornar à tela inicial do aplicativo.
        Ao ser chamado, abre tela inicial do aplicativo. Essa linha de código faz com que a interface 
        retorne à tela inicial, permitindo que o usuário navegue de volta para a tela principal após 
        realizar outras ações ou visualizar outras telas.
        """

        self.QtStack.setCurrentIndex(2)

    def abrirTelaLoginADM(self):
        """
        Abre a tela de login do administrador.

        Esse método é responsável por abrir a tela de login do administrador. 
        Ao ser chamado, abre a tela de login do administrador. Essa linha de código faz com que a
        interface mude para a tela de login do administrador, permitindo que o administrador acesse
        as funcionalidades exclusivas disponíveis para ele.
        """

        self.QtStack.setCurrentIndex(5)

    def voltarTelaADM(self):
        """
        Volta para a tela de cadastro de jogos do administrador.

        Esse método é responsável por retornar à tela de cadastro de jogos do administrador.
        Ao ser chamado, abre a tela de cadastro de jogos do administrador. Essa linha de código faz com
        que a interface retorne à tela de cadastro de jogos do administrador, permitindo que o administrador
        adicione novos jogos.
        """

        self.QtStack.setCurrentIndex(6) 

    def abrirJogos(self):
        """
        Abre a tela de jogos para o administrador.

        Esse método é responsável por abrir a tela de jogos para o administrador.
        Ao ser chamado, abre para apagar jogos para o administrador. Essa linha de código faz com que a 
        interface mude para a tela de jogos do administrador, permitindo que o administrador visualize e 
        gerencie os jogos disponíveis no sistema.
        """

        self.QtStack.setCurrentIndex(7)
        self.carregarJogosADM()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())