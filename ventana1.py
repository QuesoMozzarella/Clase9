import sys
import bcrypt

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QFormLayout, QPushButton, \
    QLineEdit, QDialog, QDialogButtonBox, QVBoxLayout
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt


class Ventana1(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Formulario de registro")

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
        self.imagenFondo = QPixmap('imagenes/alfredo.jpeg')

        # Definimos la iamgen de fondo
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        # Establecemos la distribucion de los elementos en layout horizontal
        self.horizontal = QHBoxLayout()
        # Le ponemos las margenes
        self.horizontal.setContentsMargins(30, 30, 30, 30)


        # creamos el layout del lado izquierdo

        # Creamos el layout del lado izquierdo
        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Información del cliente")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Times New Roman",20))

        # Le asignamos color de texto
        self.letrero1.setStyleSheet("color: #EFEFEF;")

        # Agregamos el letrero en la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)


        # Hacemos el letrero2
        self.letrero2 = QLabel()

        # Establecemos el ancho del label
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero2.setFont(QFont("Times New Roman", 15))

        # Le asignamos color de texto y margenes
        self.letrero2.setStyleSheet("color: #EFEFEF; margin-botton: 40px;"
                                    "margin-top: 20px;"
                                    "padding-botton: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero2 en la fila siguiente
        self.ladoIzquierdo.addRow(self.letrero2)


        # creamos los campos
        self.labelNombreCompleto = QLabel("Nombre Completo*")
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.labelNombreCompleto.setStyleSheet("color: #EFEFEF")
        self.labelNombreCompleto.setFont(QFont("Times New Roman", 12))

        self.ladoIzquierdo.addRow(self.labelNombreCompleto, self.nombreCompleto)

        # Hacemos el campo para ingresar el usuario
        self.labelUsuario = QLabel("Usuario*")
        self.usuario = QLineEdit()
        self.labelUsuario.setStyleSheet("color: #EFEFEF")
        self.labelUsuario.setFont(QFont("Times New Roman", 12))
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow(self.labelUsuario, self.usuario)

        # Hacemos el campo para ingresar el password
        self.labelPassword = QLabel("Password*")
        self.password = QLineEdit()
        self.labelPassword.setStyleSheet("color: #EFEFEF")
        self.labelPassword.setFont(QFont("Times New Roman", 12))
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow(self.labelPassword, self.password)


        # Hacemos el campo para ingresar el password2
        self.labelPassword2 = QLabel("Password*")
        self.password2 = QLineEdit()
        self.labelPassword2.setStyleSheet("color: #EFEFEF")
        self.labelPassword2.setFont(QFont("Times New Roman", 12))
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario
        self.ladoIzquierdo.addRow(self.labelPassword2, self.password2)


        # Hacemos el campo para ingresar el documento
        self.labelDocumento = QLabel("Documento*")
        self.documento = QLineEdit()
        self.labelDocumento.setFont(QFont("Times New Roman", 12))
        self.labelDocumento.setStyleSheet("color: #EFEFEF")
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario
        self.ladoIzquierdo.addRow(self.labelDocumento, self.documento)

        # Hacemos el campo para ingresar el correo
        self.labelCorreo = QLabel("Correo*")
        self.correo = QLineEdit()
        self.labelCorreo.setFont(QFont("Times New Roman", 12))
        self.labelCorreo.setStyleSheet("color: #EFEFEF")
        self.correo.setFixedWidth(250)

        # Agregamos el correo en el formulario
        self.ladoIzquierdo.addRow(self.labelCorreo, self.correo)

        # Hacemos el boton registrar los datos
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del boton
        self.botonRegistrar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonRegistrar.setStyleSheet("background-color: #008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)


        # Hacemos el boton limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        # Establecemos el ancho del boton
        self.botonLimpiar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonLimpiar.setStyleSheet("background-color: #008845;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al layout ladoIzquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layout ladoIzquierdo al layout hotizontal
        self.horizontal.addLayout(self.ladoIzquierdo)


        # Creamos el layout del lado derecho
        self.ladoDerecho = QFormLayout()

        # Se asigna la margen a la izquierda
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero3
        self.letrero3 = QLabel()

        # Le escribimos el texto
        self.letrero3.setText("Recuperar contraseña")

        # Le asignamos el tipo de letra
        self.letrero3.setFont(QFont("Times New Roman", 20))

        # Le ponemos color de texto
        self.letrero3.setStyleSheet("color: #EFEFEF;")

        # Agregamos el letrero en la primera fila
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero4
        self.letrero4 = QLabel()

        # Establecemos el ancho del label
        self.letrero4.setFixedWidth(400)

        # Le escribimos el texto
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le asignamos el tipo de letra
        self.letrero4.setFont(QFont("Times New Roman", 15))

        # Le asignamos color de texto y margenes
        self.letrero4.setStyleSheet("color: #EFEFEF; margin-botton: 40px;"
                                    "margin-top: 20px;"
                                    "padding-botton: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero4 en la fila siguiente
        self.ladoDerecho.addRow(self.letrero4)

        # Hacemos el letrero de la pregunta 1
        self.labelPregunta1 = QLabel("Pregunta de verificación 1*")
        self.labelPregunta1.setFont(QFont("Times New Roman", 12))
        self.labelPregunta1.setStyleSheet("color: #EFEFEF")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta 1
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos el correo en el formulario
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respuesta 1
        self.labelRespuesta1 = QLabel("Respuesta de verificación 1*")
        self.labelRespuesta1.setFont(QFont("Times New Roman", 12))
        self.labelRespuesta1.setStyleSheet("color: #EFEFEF")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta 1
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta1)



        # Hacemos el letrero de la pregunta 2
        self.labelPregunta2 = QLabel("Pregunta de verificación 2*")
        self.labelPregunta2.setFont(QFont("Times New Roman", 12))
        self.labelPregunta2.setStyleSheet("color: #EFEFEF")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta 1
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos el correo en el formulario
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respuesta 2
        self.labelRespuesta2 = QLabel("Respuesta de verificación 2*")
        self.labelRespuesta2.setFont(QFont("Times New Roman", 12))
        self.labelRespuesta2.setStyleSheet("color: #EFEFEF")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta 2
        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta2)


        # Hacemos el letrero de la pregunta 2
        self.labelPregunta3 = QLabel("Pregunta de verificación 3*")
        self.labelPregunta3.setFont(QFont("Times New Roman", 12))
        self.labelPregunta3.setStyleSheet("color: #EFEFEF")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta 3
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos el correo en el formulario
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respuesta 3
        self.labelRespuesta3 = QLabel("Respuesta de verificación 3*")
        self.labelRespuesta3.setFont(QFont("Times New Roman", 12))
        self.labelRespuesta3.setStyleSheet("color: #EFEFEF")

        # Agregamos el letrero en la fila siguiente
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta 3
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos el campo en el formulario
        self.ladoDerecho.addRow(self.respuesta3)



        # BOTON BUSCAR
        # Hacemos el boton para buscar las preguntas
        self.botonBuscar = QPushButton("Buscar")

        # Establecemos el ancho del boton
        self.botonBuscar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonBuscar.setStyleSheet("background-color: #008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # BOTON RECUPERAR
        # Hacemos el boton para recuperar la contraseña
        self.botonRecuperar = QPushButton("Recuperar")

        # Establecemos el ancho del boton
        self.botonRecuperar.setFixedWidth(90)

        # Le ponemos los estilos
        self.botonRecuperar.setStyleSheet("background-color: #008845;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)

        # Agregamos los dos botones al layout ladoIzquierdo
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        # Agregamos el layout ladoDerecho al layout horizontal
        self.horizontal.addLayout(self.ladoDerecho)

        # PONER AL FINAL
        # indicamos que el layout principal del fondo es horizontal
        self.fondo.setLayout(self.horizontal)


    def accion_botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion_botonRegistrar(self):

        # Creamos la ventana de dialogo
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana
        self.ventanaDialogo.resize(300, 150)

        # Creamos el boton para aceptar
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)
        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes
        self.mensaje = QLabel("")
        self.mensaje.setStyleSheet("background-color: grey; color: black; padding: 10px;")
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.opciones)
        self.ventanaDialogo.setLayout(self.vertical)

        # Variable para controlar que se han ingresado los datos correctos
        self.datosCorrectos = True

        # Validamos que los passwords sean iguales
        if (self.password.text() != self.password2.text()):
            self.datosCorrectos = True

            # Escribimos el texto explicativo
            self.mensaje.setText("Los passwords no son iguales")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            # Validamos que se ingresen todos los campos

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.password2.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):

            self.datosCorrectos = False

            # Establecemos el texto explicativo
            self.mensaje.setText("Debe ingresar todos los campos")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()
        self.passwordIngresada = self.password.text().replace(" ", "")
        # Si los datos estan correcto
        if self.datosCorrectos:

            # Abrimos el archivo en modo agregar escribidno datos en binario
            self.file = open('datos/clientes.txt', 'ab')

            cifrado_contraseña = bcrypt.hashpw(self.passwordIngresada.encode(), bcrypt.gensalt())
            # Trae el texto de los QLineEdit() y los agrupa concatenados
            # Para escribir en el archivo en formato binario UTF-8
            with open('datos/clientes.txt', 'ab') as file:
                data = (
                        self.nombreCompleto.text() + ";" +
                        self.usuario.text() + ";" +
                        self.password.text() + ";" +
                        self.password2.text() + ";" +
                        self.documento.text() + ";" +
                        self.correo.text() + ";" +
                        self.pregunta1.text() + ";" +
                        self.respuesta1.text() + ";" +
                        self.pregunta2.text() + ";" +
                        self.respuesta2.text() + ";" +
                        self.pregunta3.text() + ";" +
                        self.respuesta3.text() + "\n"
                )
                file.write(data.encode('utf-8'))
            # Cerrar archivo
            self.file.close()


            # Abrimos en modo lectura en formato bytes
            self.file = open('datos/clientes.txt', 'rb')
            # Recorrer el archivo liena por lines
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '': # Para cuando encuentre una linea vacia
                    break
            self.file.close()


    def accion_botonBuscar(self):
        print("Funcion no implementada")


    def accion_botonRecuperar(self):
        print("Funcion no implementada")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())
