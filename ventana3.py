from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QMainWindow


class Ventana3(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self,parent=None):
        super(Ventana3,self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Forma Tabular")

        # Ponemos el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # Establecemos las propiedades de ancho por alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la venata
        self.resize(self.ancho, self.alto)

        # Centrar la ventana en la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el tamaño de la ventana para evitar cambiarlo
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)


        # Establecemos el fondo principal
        self.fondo = QLabel(self)
        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/Gatos.jpg')
        # Definimos la iamgen de fondo
        self.fondo.setPixmap(self.imagenFondo)
        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)
        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)