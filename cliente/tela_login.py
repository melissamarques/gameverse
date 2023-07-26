from PyQt5 import QtCore, QtGui, QtWidgets


class TelaLogin(object):
    """
    Configura a interface do usuário para a tela de login do usuário.

    ...

    Methods
    -------
    setupUi(self, MainWindow)
        Configura a interface gráfica da janela principal.

    retranslateUi(self, MainWindow)
        Configura as traduções dos textos exibidos na interface do usuário.
    """

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
        MainWindow.resize(639, 443)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 151, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 71, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 140, 201, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 140, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 180, 51, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 180, 201, 21))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 270, 111, 21))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 270, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)

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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">GameVerse</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Entrar"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Login</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Usuário:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Senha:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Novo por aqui?</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Cadastre-se"))
        self.pushButton_4.setText(_translate("MainWindow", "Administrador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaLogin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
