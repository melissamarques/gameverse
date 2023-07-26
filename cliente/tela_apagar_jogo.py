from PyQt5 import QtCore, QtGui, QtWidgets


class TelaApagarJogo(object):
    """
    Configura a interface do usuário para a tela apagar jogos do administrador.

    ...

    Methods
    -------
    def setupUi(self, MainWindow)
        Configura a interface gráfica da janela principal.

    def retranslateUi(self, MainWindow)
        Configura as traduções dos textos exibidos na interface do usuário.
    """

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
        MainWindow.resize(640, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 461, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 601, 351))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 40, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Voltar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Nome:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Pesquisar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaApagarJogo()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
