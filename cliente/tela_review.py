from PyQt5 import QtCore, QtGui, QtWidgets

class TelaReview(QtWidgets.QDialog):
    """
    Configura a interface do usuário para a tela de escrita de review.

    ...

    Methods
    -------
    __init__(self, parent=None)
        Inicializa a janela TelaReview.

    getReview(self)
        Retorna o conteúdo do campo de texto da review.
    """

    def __init__(self, parent=None):
        """
        Inicializa a janela TelaReview.

        Parameters
        ----------
        parent : QWidget, optional
            O widget pai da janela (default é None).
        """

        super(TelaReview, self).__init__(parent)

        self.setWindowTitle('Escrever Review')
        self.resize(300, 200)

        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QtWidgets.QLabel('Digite sua avaliação:')
        self.layout.addWidget(self.label)

        self.textEdit = QtWidgets.QTextEdit()
        self.textEdit.setFixedHeight(100)
        self.layout.addWidget(self.textEdit)

        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

    def getReview(self):
        """
        Retorna o conteúdo do campo de texto da review.

        Returns
        -------
        str
            O conteúdo do campo de texto da review.
        """
        
        return self.textEdit.toPlainText()
