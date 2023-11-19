import math

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QWidget, QGridLayout, \
    QButtonGroup, QPushButton

from cliente import Cliente

class Ventana2(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self,parent=None):
        super(Ventana2,self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Usuarios Registrados")

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
        self.imagenFondo = QPixmap('imagenes/GATO.png')
        # Definimos la iamgen de fondo
        self.fondo.setPixmap(self.imagenFondo)
        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)
        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        # distribucion de los elementos
        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Ver los usuarios registrados")
        self.letrero1.setFont(QFont("Times New Roman", 20))
        self.letrero1.setStyleSheet('color: #EFEFEF')
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # creamos un scroll
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet('background-color: transparent;')
        self.scrollArea.setWidgetResizable(True)

        # creamos una ventana contenedora para cada celda
        self.contenedora = QWidget()
        # creamos un latout de grid para poner la cuadricula de elemento
        self.cuadricula = QGridLayout(self.contenedora)
        # metemos la cuadricula en el scroll
        self.scrollArea.setWidget(self.contenedora)
        # metemos el layout vertical en el scroll
        self.vertical.addWidget(self.scrollArea)

        # abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt','rb')
        # creamos una lista vacia para guardar todos los usuarios
        usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista de 11 datos separados por ;
            lista = linea.split(";")
            # para pausar si ya no hay mas registros en el archivo
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u
            u = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],
                        lista[9], lista[10], )

            # metemos el objeto en la lista de usuarios
            usuarios.append(u)

        self.file.close()

        # obtenemos el numero de usuarios registrados
        self.numeroUsuarios = len(usuarios)

        # variable contadora para controlar los usuarios en la lista usuarios
        self.contador = 0

        # definimos la cantidad de elementos por columna
        self.elementosPorColumna = 3

        # calulamos el numero de pasteles
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # controlamos los votones por una variable
        self.botones = QButtonGroup()

        # definimos que  el controlador de los botones debe agrupar a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                # validamos que se ingrese la candiad de usuarios correctos
                if self.contador < self.numeroUsuarios:
                    # en cada celda de la cuadricula va una ventana
                    self.ventanaAuxiliar = QWidget()
                    # determinar el ancho y el alto
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # creamos un layour vertical para cada cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    # creamos un voton por cada usuario mostrando su cedula
                    self.botonAccion = QPushButton(usuarios[self.contador].documento)
                    # ponemos el ancho de la galleta
                    self.botonAccion.setFixedWidth(150)
                    # ponemos sabor a la calleta
                    self.botonAccion.setStyleSheet("background-color: #EFEFEF;"
                                                   "color: black;"
                                                   "padding: 10px")
                    # metemos el boton en el layout vertical para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # agregamos el boton al grupo con su cedula como id
                    self.botones.addButton(self.botonAccion, int(usuarios[self.contador].documento))

                    self.verticalCuadricula.addStretch()

                    # a la ventana le asignamos el layout vertical
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # a la cuadricula le agregamos la ventana en la fila y columnna actual
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila , columna)

                    # aumentamos el contador
                    self.contador += 1

        # establecemos el metodo para que funcionene todos los postres
        self.botones.idClicked.connect(self.metodo_accionBotones)

















        # poner al final
        self.fondo.setLayout(self.vertical)


    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)