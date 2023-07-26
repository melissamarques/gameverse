from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import pyqtSignal, QObject


class TelaInicial(QObject):
    """
    Configura a interface do usuário para a tela inicial.

    ...

    Attributes
    ----------
    jogoSelecionado : pyqtSignal
        O sinal emitido quando um jogo é selecionado.

    Methods
    -------
    setupUi(self, MainWindow)
        Configura a interface gráfica da janela principal.

    retranslateUi(self, MainWindow)
        Configura as traduções dos textos exibidos na interface do usuário.
    """

    jogoSelecionado = pyqtSignal(int)

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
        MainWindow.resize(649, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 41, 621, 301))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 111, 21))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(480, 380, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 350, 531, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 350, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 380, 61, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">GameVerse</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Perfil"))
        self.pushButton_2.setText(_translate("MainWindow", "Sair"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Nome"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Desenvolvedora"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Distribuidora"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Ano de Lançamento"))
        self.pushButton_3.setText(_translate("MainWindow", "Pesquisar"))
        self.label_2.setText(_translate("MainWindow", "Filtrar por:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaInicial()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
