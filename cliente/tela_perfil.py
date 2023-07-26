from PyQt5 import QtCore, QtGui, QtWidgets


class TelaPerfil(QtWidgets.QMainWindow):
    """
    Configura a interface do usuário para a tela de perfil.

    ...

    Methods
    -------
    __init__()
        Inicializa a janela TelaPerfil.

    setupUi(self, MainWindow)
        Configura a interface gráfica da janela principal.

    retranslateUi(self, MainWindow)
        Configura as traduções dos textos exibidos na interface do usuário.
    """

    def __init__(self):
        """
        Inicializa a janela TelaPerfil.
        """

        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        """
        Configura a interface gráfica da janela principal.

        Essa função configura a interface gráfica da janela principal. Ela define os componentes da
        interface, suas posições e estilos.

        Parameters
        ----------
        MainWindow : QtWidgets.QMainWindow
            O objeto da janela principal.
        """

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Layout vertical principal
        self.verticalLayoutMain = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")
        self.verticalLayoutMain.setAlignment(QtCore.Qt.AlignTop)

        # Layout horizontal para os botões no topo
        self.horizontalLayoutButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutButtons.setObjectName("horizontalLayoutButtons")
        self.horizontalLayoutButtons.setAlignment(QtCore.Qt.AlignLeft)

        # Botão "Sair"
        self.sairButton = QtWidgets.QPushButton(self.centralwidget)
        self.sairButton.setObjectName("sairButton")
        self.sairButton.setText("Sair")
        self.sairButton.setMaximumWidth(80)
        self.sairButton.setStyleSheet("font-size: 12px;")
        self.horizontalLayoutButtons.addWidget(self.sairButton)

        # Espaçador vazio para posicionar os botões à esquerda
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutButtons.addItem(self.spacerItem)

        # Botão "Página Inicial"
        self.paginaInicialButton = QtWidgets.QPushButton(self.centralwidget)
        self.paginaInicialButton.setObjectName("paginaInicialButton")
        self.paginaInicialButton.setText("Página Inicial")
        self.paginaInicialButton.setMaximumWidth(120)
        self.paginaInicialButton.setStyleSheet("font-size: 12px;")
        self.horizontalLayoutButtons.addWidget(self.paginaInicialButton)

        self.verticalLayoutMain.addLayout(self.horizontalLayoutButtons)

        # Criação do layout vertical para as informações do perfil
        self.verticalLayoutProfile = QtWidgets.QVBoxLayout()
        self.verticalLayoutProfile.setObjectName("verticalLayoutProfile")

        # Layout horizontal para posicionar o nome de usuário no meio
        self.horizontalLayoutProfile = QtWidgets.QHBoxLayout()
        self.horizontalLayoutProfile.setObjectName("horizontalLayoutProfile")
        self.verticalLayoutProfile.addLayout(self.horizontalLayoutProfile)

        # Espaçador vazio para posicionar o nome de usuário no meio
        self.spacerItemProfile = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutProfile.addItem(self.spacerItemProfile)

        # Label para exibir o nome de usuário
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usernameLabel.setStyleSheet("font-size: 14px;")
        self.horizontalLayoutProfile.addWidget(self.usernameLabel)

        # Espaçador vazio para posicionar o nome de usuário no meio
        self.horizontalLayoutProfile.addItem(self.spacerItemProfile)

        # Adiciona o layout vertical do perfil ao layout vertical principal
        self.verticalLayoutMain.addLayout(self.verticalLayoutProfile)

        # Título "Últimas Reviews"
        self.reviewsLabel = QtWidgets.QLabel(self.centralwidget)
        self.reviewsLabel.setObjectName("reviewsLabel")
        self.reviewsLabel.setText("Últimas Reviews")
        self.reviewsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayoutMain.addWidget(self.reviewsLabel)

        # Lista de reviews
        self.reviewsList = QtWidgets.QListWidget(self.centralwidget)
        self.reviewsList.setObjectName("reviewsList")
        self.verticalLayoutMain.addWidget(self.reviewsList)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Perfil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaPerfil()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
