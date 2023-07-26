from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from cliente import Cliente

class TelaJogo(QtWidgets.QMainWindow):
    """
    Configura a interface do usuário para a tela do jogo.

    ...

    Attributes
    ----------
    jogo_id : int
        O ID do jogo específico.

    Methods
    -------
    def __init__(self, jogo_id)
        Inicializa a janela TelaJogo.

    def setupUi(self, MainWindow)
        Configura a interface gráfica da janela principal.

    def retranslateUi(self, MainWindow)
        Configura as traduções dos textos exibidos na interface do usuário.
    """

    def __init__(self, jogo_id):
        """
        Inicializa a janela TelaJogo.

        Parameters
        ----------
        jogo_id : int
            O ID do jogo.
        """

        super().__init__()
        self.jogo_id = jogo_id
        self.setupUi(self)
    
    def setupUi(self, MainWindow):
        """
        Configura a interface gráfica da janela principal.

        Essa função configura a interface gráfica da janela principal. Essa função é chamada
        para configurar a interface gráfica da janela principal e definir os componentes e suas posições na tela.

        Parameters
        ----------
        MainWindow : QtWidgets.QMainWindow
            O objeto da janela principal.
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Criação do layout vertical principal
        self.verticalLayoutMain = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.verticalLayoutMain.setAlignment(QtCore.Qt.AlignTop)  # Alinhamento ao topo

        # Criação do layout horizontal para os botões
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        self.horizontalLayoutButtons.setAlignment(QtCore.Qt.AlignLeft)  # Alinhamento à esquerda

        # Botão "Voltar"
        self.voltarButton = QtWidgets.QPushButton(self.centralwidget)
        self.voltarButton.setObjectName("voltarButton")
        self.voltarButton.setText("Voltar")
        self.voltarButton.setMaximumWidth(80)  # Definir largura máxima do botão
        self.voltarButton.setStyleSheet("font-size: 12px;")  # Definir tamanho da fonte


        # Adiciona o botão "Voltar" ao layout horizontal dos botões
        self.horizontalLayoutButtons.addWidget(self.voltarButton)

        # Botão "Sair"
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setObjectName("sairButton")
        self.sairButton.setText("Sair")
        self.sairButton.setMaximumWidth(80)  # Definir largura máxima do botão
        self.sairButton.setStyleSheet("font-size: 12px;")  # Definir tamanho da fonte

        
        # Adiciona o botão "Sair" ao layout horizontal dos botões
        self.horizontalLayoutButtons.addWidget(self.sairButton)

        # Espaçador vazio para posicionar o botão "Perfil" no canto superior direito
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(self.spacerItem)

        # Botão "Perfil"
        self.perfilButton = QtWidgets.QPushButton(self.centralwidget)
        self.perfilButton.setObjectName("perfilButton")
        self.perfilButton.setText("Perfil")
        self.perfilButton.setMaximumWidth(80)  # Definir largura máxima do botão
        self.perfilButton.setStyleSheet("font-size: 12px;")  # Definir tamanho da fonte

        # Adiciona o botão "Perfil" ao layout horizontal dos botões
        self.horizontalLayoutButtons.addWidget(self.perfilButton)

        # Adiciona o layout horizontal dos botões ao layout vertical principal
        self.verticalLayoutMain.addLayout(self.horizontalLayoutButtons)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)  # Alinhamento ao topo e ao centro
        self.label.setObjectName("label")

        # Definir estilo CSS para o label (nome do jogo)
        self.label.setStyleSheet("font-size: 20px; font-weight: bold;")

        # Adiciona o label ao layout vertical principal
        self.verticalLayoutMain.addWidget(self.label)

        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setWordWrap(True)

        # Adiciona o infoLabel ao layout vertical principal
        self.verticalLayoutMain.addWidget(self.infoLabel)

        # Criação do layout horizontal para os botões adicionais
        self.horizontalLayoutAdditionalButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutAdditionalButtons.setObjectName("horizontalLayoutAdditionalButtons")
        self.horizontalLayoutAdditionalButtons.setAlignment(QtCore.Qt.AlignCenter)  # Alinhamento ao centro

        # Botão "Review"
        self.reviewButton = QtWidgets.QPushButton(self.centralwidget)
        self.reviewButton.setObjectName("reviewButton")
        self.reviewButton.setText("Review")
        self.reviewButton.setMaximumWidth(120)  # Definir largura máxima do botão
        self.reviewButton.setStyleSheet("font-size: 12px;")  # Definir tamanho da fonte

        # Adiciona o botão "Review" ao layout horizontal dos botões adicionais
        self.horizontalLayoutAdditionalButtons.addWidget(self.reviewButton)

        # Adiciona o layout horizontal dos botões adicionais ao layout vertical principal
        self.verticalLayoutMain.addLayout(self.horizontalLayoutAdditionalButtons)

        self.reviewsList = QtWidgets.QListWidget(self.centralwidget)
        self.reviewsList.setObjectName("reviewsList")
        self.verticalLayoutMain.addWidget(self.reviewsList)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.carregarInformacoes(self.jogo_id)


    def retranslateUi(self, MainWindow):
        """
        Configura as traduções dos textos exibidos na interface do usuário.

        Essa função configura as traduções dos textos exibidos na interface
        do usuário. Essa função é responsável por configurar as traduções dos textos na
        interface do usuário, permitindo que o aplicativo exiba os textos em diferentes idiomas. 

        Parameters
        ----------
        MainWindow : QtWidgets.QMainWindow
            O objeto da janela principal.
        """

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Página do Jogo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaJogo(1)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())