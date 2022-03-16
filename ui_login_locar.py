from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
        
    def setupUi(self, MainWindow):

        #EXPS REGULARES
        ##########################################################
        #VALIDADOR INTEIRO
        self.validaInteiro = QRegularExpressionValidator(QRegularExpression("[0-9]*"))
        #VALIDADOR NOME
        self.validaNome = QRegularExpressionValidator(QRegularExpression("[a-zA-z çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ-]*"))
        #VALIDADOR TEXTO
        self.validaTexto = QRegularExpressionValidator(QRegularExpression("[a-zA-z0-9 çáàãâéíóôõúÇÁÀÃÂÉÍÓÔÕÚ\\.-]*"))
        #VALIDADOR EMAIL
        self.validaEmail = QRegularExpressionValidator(QRegularExpression("([a-z0-9]+[.-_])*[a-z0-9]+@[a-z]+(\\.[a-z]{2,})+"))
        #VALIDADOR PLACA-CARRO
        self.validaPlaca = QRegularExpressionValidator(QRegularExpression("[a-z]{3}-[0-9]{4}"))
        #VALIDADOR CPF
        self.validaCPF = QRegularExpressionValidator(QRegularExpression("([0-9]{3}\\.){2}[0-9]{3}-[0-9]{2}"))
        #VALIDAR ANO
        self.validaAno = QRegularExpressionValidator(QRegularExpression("[0-9]{4}"))
        ##########################################################

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 200))
        self.frame_2.setMaximumSize(QSize(300, 200))
        self.frame_2.setStyleSheet(u"image: url(logo-locar.png);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 100))
        self.frame_5.setMaximumSize(QSize(200, 400))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(100, 100))
        self.frame_3.setMaximumSize(QSize(100, 100))
        self.frame_3.setStyleSheet(u"image: url(perfil.svg);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.email_login = QLineEdit(self.frame_4)
        self.email_login.setObjectName(u"lineEdit")
        self.email_login.setValidator(self.validaEmail)
        self.email_login.setMaxLength(50)
        self.email_login.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.email_login)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)
        self.senha_login = QLineEdit(self.frame_4)
        self.senha_login.setObjectName(u"lineEdit_2")
        self.senha_login.setValidator(self.validaTexto)
        self.senha_login.setMaxLength(16)
        self.senha_login.setEchoMode(QLineEdit.Password)
        self.senha_login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        

        self.verticalLayout.addWidget(self.senha_login)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_3 = QHBoxLayout(self.page_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(100, 0))
        self.frame_7.setMaximumSize(QSize(100, 16777215))
        self.frame_7.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.frame_7)
        self.btn_home.setObjectName(u"pushButton")
        self.btn_home.setCursor(Qt.PointingHandCursor)
        self.btn_home.setMinimumSize(QSize(75, 75))
        self.btn_home.setMaximumSize(QSize(75, 75))
        self.btn_home.setStyleSheet(u"QPushButton:focus{outline:0; background-color:rgb(255, 201, 6);} QPushButton:hover{background-color:rgb(255, 201, 6);}"
                                            "QPushButton{image: url(logo-locar); border: hidden}")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.verticalSpacer_2 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_c_carro = QPushButton(self.frame_7)
        self.btn_c_carro.setObjectName(u"btn_c_carro")
        self.btn_c_carro.setCursor(Qt.PointingHandCursor)
        self.btn_c_carro.setMinimumSize(QSize(75, 75))
        self.btn_c_carro.setMaximumSize(QSize(75, 75))
        self.btn_c_carro.setStyleSheet(u"QPushButton:focus{outline:0; background-color:rgb(255, 201, 6);} QPushButton:hover{background-color:rgb(255, 201, 6);}"
                                            "QPushButton{image: url(carro.svg); border: hidden}")

        self.verticalLayout_4.addWidget(self.btn_c_carro)

        self.btn_c_funcionario = QPushButton(self.frame_7)
        self.btn_c_funcionario.setObjectName(u"btn_c_funcionario")
        self.btn_c_funcionario.setCursor(Qt.PointingHandCursor)
        self.btn_c_funcionario.setMinimumSize(QSize(75, 75))
        self.btn_c_funcionario.setMaximumSize(QSize(75, 75))
        self.btn_c_funcionario.setStyleSheet(u"QPushButton:focus{outline:0; background-color:rgb(255, 201, 6);} QPushButton:hover{background-color:rgb(255, 201, 6);}"
                                                        "QPushButton{image: url(add-funcio.svg); border: hidden}")

        self.verticalLayout_4.addWidget(self.btn_c_funcionario)

        self.btn_c_aluguel = QPushButton(self.frame_7)
        self.btn_c_aluguel.setObjectName(u"btn_c_aluguel")
        self.btn_c_aluguel.setCursor(Qt.PointingHandCursor)
        self.btn_c_aluguel.setMinimumSize(QSize(75, 75))
        self.btn_c_aluguel.setMaximumSize(QSize(75, 75))
        self.btn_c_aluguel.setStyleSheet(u"QPushButton:focus{outline:0; background-color:rgb(255, 201, 6);} QPushButton:hover{background-color:rgb(255, 201, 6);}"
                                                        "QPushButton{image: url(aluguel.svg); border: hidden}")

        self.verticalLayout_4.addWidget(self.btn_c_aluguel)

        self.btn_c_cliente = QPushButton(self.frame_7)
        self.btn_c_cliente.setObjectName(u"btn_c_cliente")
        self.btn_c_cliente.setCursor(Qt.PointingHandCursor)
        self.btn_c_cliente.setMinimumSize(QSize(75, 75))
        self.btn_c_cliente.setMaximumSize(QSize(75, 75))
        self.btn_c_cliente.setStyleSheet(u"QPushButton:focus{outline:0; background-color:rgb(255, 201, 6);} QPushButton:hover{background-color:rgb(255, 201, 6);}"
                                                        "QPushButton{image: url(cliente.svg); border: hidden}")

        self.verticalLayout_4.addWidget(self.btn_c_cliente)

        self.verticalSpacer_3 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.btn_logout = QPushButton(self.frame_7)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setCursor(Qt.PointingHandCursor)
        self.btn_logout.setMinimumSize(QSize(35, 35))
        self.btn_logout.setStyleSheet(u"QPushButton:focus{outline:0} QPushButton:hover{background-color:rgb(255, 201, 6);}"
                                                        "QPushButton{image: url(logout.svg); border: hidden}")

        self.verticalLayout_4.addWidget(self.btn_logout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addWidget(self.frame_7)

        self.stackedWidget_2 = QStackedWidget(self.page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.c_carro = QWidget()
        self.c_carro.setObjectName(u"c_aluguel")
        self.verticalLayout_10 = QVBoxLayout(self.c_carro)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.c_carro)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(800, 600))
        self.frame_6.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_16)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 400))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_15)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(20, 180, 300, 75))
        self.frame_14.setMinimumSize(QSize(300, 0))
        self.frame_14.setMaximumSize(QSize(300, 75))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_14)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_17)

        self.label_VALOR = QLabel(self.frame_14)
        self.label_VALOR.setObjectName(u"label_VALOR")
        self.label_VALOR.setMaximumSize(QSize(16777215, 75))

        self.verticalLayout_9.addWidget(self.label_VALOR)

        self.lineEdit_VALOR = QLineEdit(self.frame_14)
        self.lineEdit_VALOR.setObjectName(u"lineEdit_VALOR")
        self.lineEdit_VALOR.setValidator(self.validaInteiro)
        self.lineEdit_VALOR.setPlaceholderText("00.00")
        self.lineEdit_VALOR.setMinimumSize(QSize(200, 25))
        self.lineEdit_VALOR.setMaximumSize(QSize(300, 25))
        self.lineEdit_VALOR.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.lineEdit_VALOR)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_18)

        self.frame_13 = QFrame(self.frame_15)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(20, 99, 300, 75))
        self.frame_13.setMinimumSize(QSize(300, 0))
        self.frame_13.setMaximumSize(QSize(300, 75))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)

        self.label_ANO = QLabel(self.frame_13)
        self.label_ANO.setObjectName(u"label_ANO")

        self.verticalLayout_8.addWidget(self.label_ANO)

        self.lineEdit_ANO = QLineEdit(self.frame_13)
        self.lineEdit_ANO.setObjectName(u"lineEdit_ANO")
        self.lineEdit_ANO.setValidator(self.validaAno)
        self.lineEdit_ANO.setPlaceholderText("aaaa")
        self.lineEdit_ANO.setMaxLength(4)
        self.lineEdit_ANO.setMinimumSize(QSize(200, 25))
        self.lineEdit_ANO.setMaximumSize(QSize(300, 25))
        self.lineEdit_ANO.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.lineEdit_ANO)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_15)

        self.frame_10 = QFrame(self.frame_15)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(20, 18, 300, 75))
        self.frame_10.setMinimumSize(QSize(300, 0))
        self.frame_10.setMaximumSize(QSize(300, 75))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.label_MODELO = QLabel(self.frame_10)
        self.label_MODELO.setObjectName(u"label_MODELO")

        self.verticalLayout_6.addWidget(self.label_MODELO)

        self.lineEdit_MODELO = QLineEdit(self.frame_10)
        self.lineEdit_MODELO.setObjectName(u"lineEdit_MODELO")
        self.lineEdit_MODELO.setValidator(self.validaTexto)
        self.lineEdit_MODELO.setMaxLength(50)
        self.lineEdit_MODELO.setMinimumSize(QSize(200, 25))
        self.lineEdit_MODELO.setMaximumSize(QSize(300, 25))
        self.lineEdit_MODELO.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_6.addWidget(self.lineEdit_MODELO)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.frame_11 = QFrame(self.frame_15)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(340, 180, 315, 75))
        self.frame_11.setMinimumSize(QSize(315, 0))
        self.frame_11.setMaximumSize(QSize(100, 75))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 0, 2, 1, 1)

        self.BTN_CANCELAR = QPushButton(self.frame_11)
        self.BTN_CANCELAR.setObjectName(u"BTN_CANCELAR")
        self.BTN_CANCELAR.setCursor(Qt.PointingHandCursor)
        self.BTN_CANCELAR.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 76, 76);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
 
"}")

        self.gridLayout_3.addWidget(self.BTN_CANCELAR, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.BTN_CONFIRMAR = QPushButton(self.frame_11)
        self.BTN_CONFIRMAR.setObjectName(u"BTN_CONFIRMAR")
        self.BTN_CONFIRMAR.setCursor(Qt.PointingHandCursor)
        self.BTN_CONFIRMAR.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
 
"}")

        self.gridLayout_3.addWidget(self.BTN_CONFIRMAR, 1, 2, 1, 1)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_14, 2, 2, 1, 1)

        self.frame_9 = QFrame(self.frame_15)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(340, 99, 315, 75))
        self.frame_9.setMinimumSize(QSize(315, 0))
        self.frame_9.setMaximumSize(QSize(300, 75))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_12)

        self.label_DESCRIAO = QLabel(self.frame_9)
        self.label_DESCRIAO.setObjectName(u"label_DESCRIAO")

        self.verticalLayout_5.addWidget(self.label_DESCRIAO)

        self.lineEdit_4DESCRIAO = QLineEdit(self.frame_9)
        self.lineEdit_4DESCRIAO.setObjectName(u"lineEdit_4DESCRIAO")
        self.lineEdit_4DESCRIAO.setValidator(self.validaTexto)
        self.lineEdit_4DESCRIAO.setMaxLength(255)
        self.lineEdit_4DESCRIAO.setPlaceholderText("Maximo 255 caracter")
        self.lineEdit_4DESCRIAO.setMinimumSize(QSize(300, 25))
        self.lineEdit_4DESCRIAO.setMaximumSize(QSize(300, 25))
        self.lineEdit_4DESCRIAO.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.lineEdit_4DESCRIAO)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_10)

        self.frame_12 = QFrame(self.frame_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(340, 18, 315, 75))
        self.frame_12.setMinimumSize(QSize(315, 0))
        self.frame_12.setMaximumSize(QSize(300, 75))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

        self.label_2PLACA = QLabel(self.frame_12)
        self.label_2PLACA.setObjectName(u"label_2PLACA")

        self.verticalLayout_7.addWidget(self.label_2PLACA)

        self.lineEdit_PLACA = QLineEdit(self.frame_12)
        self.lineEdit_PLACA.setObjectName(u"lineEdit_PLACA")
        self.lineEdit_PLACA.setValidator(self.validaPlaca)
        self.lineEdit_PLACA.setMaxLength(8)
        self.lineEdit_PLACA.setPlaceholderText("abc-0000")
        self.lineEdit_PLACA.setMinimumSize(QSize(300, 25))
        self.lineEdit_PLACA.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_PLACA.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.lineEdit_PLACA)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_9)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.stackedWidget_2.addWidget(self.c_carro)
        self.c_funcionario = QWidget()
        self.c_funcionario.setObjectName(u"c_funcionario")
        self.horizontalLayout_4 = QHBoxLayout(self.c_funcionario)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.c_funcionario)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(800, 600))
        self.frame_16.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalSpacer_30 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_30)

        self.frame_23 = QFrame(self.frame_16)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(0, 400))
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.frame_19 = QFrame(self.frame_23)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(340, 190, 315, 75))
        self.frame_19.setMinimumSize(QSize(315, 0))
        self.frame_19.setMaximumSize(QSize(100, 75))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_19)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)

        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_24, 0, 2, 1, 1)

        self.BTN_CANCELAR_2 = QPushButton(self.frame_19)
        self.BTN_CANCELAR_2.setObjectName(u"BTN_CANCELAR_2")
        self.BTN_CANCELAR_2.setCursor(Qt.PointingHandCursor)
        self.BTN_CANCELAR_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 76, 76);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
 
"}")

        self.gridLayout_4.addWidget(self.BTN_CANCELAR_2, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.BTN_CONFIRMAR_2 = QPushButton(self.frame_19)
        self.BTN_CONFIRMAR_2.setObjectName(u"BTN_CONFIRMAR_2")
        self.BTN_CONFIRMAR_2.setCursor(Qt.PointingHandCursor)
        self.BTN_CONFIRMAR_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
 
"}")

        self.gridLayout_4.addWidget(self.BTN_CONFIRMAR_2, 1, 2, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_25, 2, 2, 1, 1)

        self.frame_21 = QFrame(self.frame_23)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(20, 109, 300, 75))
        self.frame_21.setMinimumSize(QSize(300, 0))
        self.frame_21.setMaximumSize(QSize(300, 75))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_28)

        self.label_EMAIL = QLabel(self.frame_21)
        self.label_EMAIL.setObjectName(u"label_EMAIL")

        self.verticalLayout_15.addWidget(self.label_EMAIL)

        self.lineEdit_EMAIL = QLineEdit(self.frame_21)
        self.lineEdit_EMAIL.setObjectName(u"lineEdit_EMAIL")
        self.lineEdit_EMAIL.setValidator(self.validaEmail)
        self.lineEdit_EMAIL.setMaxLength(50)
        self.lineEdit_EMAIL.setMinimumSize(QSize(200, 25))
        self.lineEdit_EMAIL.setMaximumSize(QSize(300, 25))
        self.lineEdit_EMAIL.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_15.addWidget(self.lineEdit_EMAIL)

        self.verticalSpacer_29 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_29)

        self.frame_17 = QFrame(self.frame_23)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(340, 109, 315, 75))
        self.frame_17.setMinimumSize(QSize(315, 0))
        self.frame_17.setMaximumSize(QSize(300, 75))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_20)

        self.label_Senha = QLabel(self.frame_17)
        self.label_Senha.setObjectName(u"label_Senha")

        self.verticalLayout_12.addWidget(self.label_Senha)

        self.lineEdit_Senha = QLineEdit(self.frame_17)
        self.lineEdit_Senha.setObjectName(u"lineEdit_Senha")
        self.lineEdit_Senha.setValidator(self.validaTexto)
        self.lineEdit_Senha.setMaxLength(16)
        self.lineEdit_Senha.setMinimumSize(QSize(300, 25))
        self.lineEdit_Senha.setMaximumSize(QSize(300, 25))
        self.lineEdit_Senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.lineEdit_Senha)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_21)

        self.frame_18 = QFrame(self.frame_23)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(20, 28, 300, 75))
        self.frame_18.setMinimumSize(QSize(300, 0))
        self.frame_18.setMaximumSize(QSize(300, 75))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_18)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_22)

        self.label_NOME = QLabel(self.frame_18)
        self.label_NOME.setObjectName(u"label_NOME")

        self.verticalLayout_13.addWidget(self.label_NOME)

        self.lineEdit_NOME = QLineEdit(self.frame_18)
        self.lineEdit_NOME.setObjectName(u"lineEdit_NOME")
        self.lineEdit_NOME.setValidator(self.validaNome)
        self.lineEdit_NOME.setMinimumSize(QSize(200, 25))
        self.lineEdit_NOME.setMaximumSize(QSize(300, 25))
        self.lineEdit_NOME.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.lineEdit_NOME)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_23)

        self.frame_20 = QFrame(self.frame_23)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(340, 28, 315, 75))
        self.frame_20.setMinimumSize(QSize(315, 0))
        self.frame_20.setMaximumSize(QSize(300, 75))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_26 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_26)

        self.label_CPF = QLabel(self.frame_20)
        self.label_CPF.setObjectName(u"label_CPF")

        self.verticalLayout_14.addWidget(self.label_CPF)

        self.lineEdit_CPF = QLineEdit(self.frame_20)
        self.lineEdit_CPF.setObjectName(u"lineEdit_CPF")
        self.lineEdit_CPF.setValidator(self.validaCPF)
        self.lineEdit_CPF.setPlaceholderText("000.000.000-00")
        self.lineEdit_CPF.setMaxLength(14)
        self.lineEdit_CPF.setMinimumSize(QSize(300, 25))
        self.lineEdit_CPF.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_CPF.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.lineEdit_CPF)

        self.verticalSpacer_27 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_27)

        self.frame_22 = QFrame(self.frame_23)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(20, 190, 300, 75))
        self.frame_22.setMinimumSize(QSize(300, 0))
        self.frame_22.setMaximumSize(QSize(300, 75))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_22)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer_31 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_31)

        self.label_Perfil = QLabel(self.frame_22)
        self.label_Perfil.setObjectName(u"label_Perfil")
        self.label_Perfil.setMaximumSize(QSize(16777215, 75))

        self.verticalLayout_16.addWidget(self.label_Perfil)

        self.comboBox_Perfil = QComboBox(self.frame_22)
        opcao = ["Administrador", "Funcionario"] 
        self.comboBox_Perfil.addItems(opcao) 
        self.comboBox_Perfil.setObjectName(u"comboBox_Perfil")
        self.comboBox_Perfil.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.comboBox_Perfil)

        self.verticalSpacer_32 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_32)


        self.verticalLayout_17.addWidget(self.frame_23)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_19)


        self.horizontalLayout_4.addWidget(self.frame_16)

        self.stackedWidget_2.addWidget(self.c_funcionario)
        self.c_aluguel = QWidget()
        self.c_aluguel.setObjectName(u"c_carro")
        self.verticalLayout_24 = QVBoxLayout(self.c_aluguel)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.c_aluguel)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMinimumSize(QSize(800, 600))
        self.frame_24.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_24)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacer_34 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_34)

        self.frame_32 = QFrame(self.frame_24)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 400))
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.frame_32)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(340, 170, 315, 75))
        self.frame_31.setMinimumSize(QSize(315, 0))
        self.frame_31.setMaximumSize(QSize(100, 75))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_31)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 1, 3, 1, 1)

        self.verticalSpacer_47 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_47, 0, 2, 1, 1)

        self.BTN_CANCELAR_3 = QPushButton(self.frame_31)
        self.BTN_CANCELAR_3.setObjectName(u"BTN_CANCELAR_3")
        self.BTN_CANCELAR_3.setCursor(Qt.PointingHandCursor)
        self.BTN_CANCELAR_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 76, 76);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
 
"}")

        self.gridLayout_5.addWidget(self.BTN_CANCELAR_3, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 1, 0, 1, 1)

        self.BTN_CONFIRMAR_3 = QPushButton(self.frame_31)
        self.BTN_CONFIRMAR_3.setObjectName(u"BTN_CONFIRMAR_3")
        self.BTN_CONFIRMAR_3.setCursor(Qt.PointingHandCursor)
        self.BTN_CONFIRMAR_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
 
"}")

        self.gridLayout_5.addWidget(self.BTN_CONFIRMAR_3, 1, 2, 1, 1)

        self.verticalSpacer_48 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_48, 2, 2, 1, 1)

        self.frame_30 = QFrame(self.frame_32)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(20, 251, 300, 75))
        self.frame_30.setMinimumSize(QSize(300, 75))
        self.frame_30.setMaximumSize(QSize(300, 75))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_30)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSpacer_45 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.frame_29 = QFrame(self.frame_32)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(20, 170, 300, 75))
        self.frame_29.setMinimumSize(QSize(300, 0))
        self.frame_29.setMaximumSize(QSize(300, 75))
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_29)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_43 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_43)

        self.label_Perfil_2 = QLabel(self.frame_29)
        self.label_Perfil_2.setObjectName(u"label_Perfil_2")
        self.label_Perfil_2.setMaximumSize(QSize(16777215, 75))

        self.verticalLayout_22.addWidget(self.label_Perfil_2)

        self.comboBox_Perfil_2 = QComboBox(self.frame_29)
        self.comboBox_Perfil_2.addItem("")
        self.comboBox_Perfil_2.addItem("")
        self.comboBox_Perfil_2.addItem("")
        self.comboBox_Perfil_2.setObjectName(u"comboBox_Perfil_2")
        self.comboBox_Perfil_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.comboBox_Perfil_2)

        self.verticalSpacer_44 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_44)
        self.frame_27 = QFrame(self.frame_32)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(20, 8, 300, 75))
        self.frame_27.setMinimumSize(QSize(300, 0))
        self.frame_27.setMaximumSize(QSize(300, 75))
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_27)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_39 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_39)

        self.cpf_aluguel_label = QLabel(self.frame_27)
        self.cpf_aluguel_label.setObjectName(u"cpf_aluguel_label")
        
        self.verticalLayout_20.addWidget(self.cpf_aluguel_label)

        self.cpf_aluguel = QLineEdit(self.frame_27)
        self.cpf_aluguel.setObjectName(u"cpf_aluguel")
        self.cpf_aluguel.setValidator(self.validaCPF)
        self.cpf_aluguel.setMinimumSize(QSize(200, 25))
        self.cpf_aluguel.setMaximumSize(QSize(300, 25))
        self.cpf_aluguel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_20.addWidget(self.cpf_aluguel)

        self.verticalSpacer_40 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_40)

        self.frame_28 = QFrame(self.frame_32)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(20, 89, 300, 75))
        self.frame_28.setMinimumSize(QSize(300, 0))
        self.frame_28.setMaximumSize(QSize(300, 75))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_28)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalSpacer_41 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_41)

        self.data_retirada_label = QLabel(self.frame_28)
        self.data_retirada_label.setObjectName(u"data_retirada_label")

        self.verticalLayout_21.addWidget(self.data_retirada_label)

        self.data_retirada = QDateEdit(self.frame_28)
        self.data_retirada.setObjectName(u"data_retirada")
        self.data_retirada.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.data_retirada.setMinimumSize(QSize(200, 25))
        self.data_retirada.setMaximumSize(QSize(300, 25))
        self.data_retirada.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.data_retirada)

        self.verticalSpacer_42 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_42)

        self.frame_25 = QFrame(self.frame_32)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(340, 8, 315, 75))
        self.frame_25.setMinimumSize(QSize(315, 0))
        self.frame_25.setMaximumSize(QSize(300, 75))
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_25)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_35 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_35)

        self.carro = QLabel(self.frame_25)
        self.carro.setObjectName(u"carro")

        self.verticalLayout_18.addWidget(self.carro)

        self.comboBox = QComboBox(self.frame_25)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.comboBox)

        self.verticalSpacer_36 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_36)

        self.frame_26 = QFrame(self.frame_32)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(340, 89, 315, 75))
        self.frame_26.setMinimumSize(QSize(315, 0))
        self.frame_26.setMaximumSize(QSize(300, 75))
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_26)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_37 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_37)

        self.data_entrega_label = QLabel(self.frame_26)
        self.data_entrega_label.setObjectName(u"data_entrega_label")

        self.verticalLayout_19.addWidget(self.data_entrega_label)

        self.data_entrega = QDateEdit(self.frame_26)
        self.data_entrega.setObjectName(u"data_entrega")
        self.data_entrega.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.data_entrega.setMinimumSize(QSize(300, 25))
        self.data_entrega.setMaximumSize(QSize(300, 25))
        self.data_entrega.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.data_entrega)

        self.verticalSpacer_38 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_38)

        self.verticalLayout_25.addWidget(self.frame_32)

        self.verticalSpacer_33 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_33)


        self.verticalLayout_24.addWidget(self.frame_24)

        self.stackedWidget_2.addWidget(self.c_aluguel)
        self.c_cliente = QWidget()
        self.c_cliente.setObjectName(u"c_cliente")
        self.horizontalLayout_5 = QHBoxLayout(self.c_cliente)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.c_cliente)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setMinimumSize(QSize(800, 600))
        self.frame_33.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_33)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalSpacer_60 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_60)

        self.frame_39 = QFrame(self.frame_33)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 400))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.frame_37 = QFrame(self.frame_39)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(330, 20, 315, 75))
        self.frame_37.setMinimumSize(QSize(315, 0))
        self.frame_37.setMaximumSize(QSize(300, 75))
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_37)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalSpacer_56 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_56)

        self.label_CPF_cliente = QLabel(self.frame_37)
        self.label_CPF_cliente.setObjectName(u"label_CPF_cliente")

        self.verticalLayout_28.addWidget(self.label_CPF_cliente)

        self.lineEdit_CPF_cliente = QLineEdit(self.frame_37)
        self.lineEdit_CPF_cliente.setObjectName(u"lineEdit_CPF_cliente")
        self.lineEdit_CPF_cliente.setValidator(self.validaCPF)
        self.lineEdit_CPF_cliente.setPlaceholderText("000.000.000-00")
        self.lineEdit_CPF_cliente.setMinimumSize(QSize(300, 25))
        self.lineEdit_CPF_cliente.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_CPF_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_28.addWidget(self.lineEdit_CPF_cliente)

        self.verticalSpacer_57 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_28.addItem(self.verticalSpacer_57)

        self.frame_35 = QFrame(self.frame_39)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(10, 20, 300, 75))
        self.frame_35.setMinimumSize(QSize(300, 0))
        self.frame_35.setMaximumSize(QSize(300, 75))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_35)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_52 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_52)

        self.label_NOME_cliente = QLabel(self.frame_35)
        self.label_NOME_cliente.setObjectName(u"label_NOME_cliente")

        self.verticalLayout_27.addWidget(self.label_NOME_cliente)

        self.lineEdit_NOME_cliente = QLineEdit(self.frame_35)
        self.lineEdit_NOME_cliente.setObjectName(u"lineEdit_NOME_cliente")
        self.lineEdit_NOME_cliente.setValidator(self.validaNome)
        self.lineEdit_NOME_cliente.setMinimumSize(QSize(200, 25))
        self.lineEdit_NOME_cliente.setMaximumSize(QSize(300, 25))
        self.lineEdit_NOME_cliente.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_27.addWidget(self.lineEdit_NOME_cliente)

        self.verticalSpacer_53 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_53)

        self.frame_36 = QFrame(self.frame_39)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(330, 182, 315, 75))
        self.frame_36.setMinimumSize(QSize(315, 0))
        self.frame_36.setMaximumSize(QSize(100, 75))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_36)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 1, 3, 1, 1)

        self.verticalSpacer_54 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_54, 0, 2, 1, 1)

        self.BTN_CANCELAR_4 = QPushButton(self.frame_36)
        self.BTN_CANCELAR_4.setObjectName(u"BTN_CANCELAR_4")
        self.BTN_CANCELAR_4.setCursor(Qt.PointingHandCursor)
        self.BTN_CANCELAR_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 76, 76);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
"}")

        self.gridLayout_6.addWidget(self.BTN_CANCELAR_4, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 1, 0, 1, 1)

        self.BTN_CONFIRMAR_4 = QPushButton(self.frame_36)
        self.BTN_CONFIRMAR_4.setObjectName(u"BTN_CONFIRMAR_4")
        self.BTN_CONFIRMAR_4.setCursor(Qt.PointingHandCursor)
        self.BTN_CONFIRMAR_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 170, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 201, 6);\n"
"}")

        self.gridLayout_6.addWidget(self.BTN_CONFIRMAR_4, 1, 2, 1, 1)

        self.verticalSpacer_55 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_55, 2, 2, 1, 1)

        self.frame_38 = QFrame(self.frame_39)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setGeometry(QRect(10, 101, 300, 75))
        self.frame_38.setMinimumSize(QSize(300, 0))
        self.frame_38.setMaximumSize(QSize(300, 75))
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_38)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalSpacer_58 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_58)

        self.verticalSpacer_59 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_59)

        self.frame_34 = QFrame(self.frame_39)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(330, 101, 315, 75))
        self.frame_34.setMinimumSize(QSize(315, 0))
        self.frame_34.setMaximumSize(QSize(300, 75))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_34)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_50 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_50)

        self.verticalSpacer_51 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_51)

        self.verticalLayout_30.addWidget(self.frame_39)

        self.verticalSpacer_49 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_49)

        self.horizontalLayout_5.addWidget(self.frame_33)

        self.stackedWidget_2.addWidget(self.c_cliente)

          
        self.c_historico = QWidget()
        self.c_historico.setObjectName(u"c_historico")
        self.horizontalLayout_6 = QHBoxLayout(self.c_historico)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.frame_30 = QFrame(self.c_historico)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: rgb(85, 255, 255);")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.alugados = QFrame(self.frame_30)
        self.alugados.setObjectName(u"alugados")
        self.alugados.setFrameShape(QFrame.StyledPanel)
        self.alugados.setFrameShadow(QFrame.Raised)
        self.tabela = QTableWidget(self.alugados)
        if (self.tabela.columnCount() < 4):
            self.tabela.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela.setObjectName(u"tabela")
        self.tabela.setGeometry(QRect(120, 70, 400, 471))

        self.tabela.horizontalHeader().setStyleSheet(u"QHeaderView::Section{padding-bottom: 16px; padding-top: 8px; background-color: #FFF; border:hidden}")
        self.tabela.setStyleSheet(u"QTableView{border: hidden;} QTableView::item{outline: 0;}")
        self.tabela.verticalHeader().setVisible(False)
        self.tabela.horizontalHeader().setHighlightSections(False)
        self.tabela.setAlternatingRowColors(True)
        self.tabela.setShowGrid(False)
        self.tabela.setFocusPolicy(Qt.NoFocus)
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela.setSortingEnabled(False)
        self.tabela.setEditTriggers(QAbstractItemView.NoEditTriggers) #Disabilita todos os triggers
        self.tabela.setTabKeyNavigation(False) # Desabilita tab key na tabela

        self.tabela.setMaximumSize(QSize(400, 16777215))
        self.tabela.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_31 = QFrame(self.alugados)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(450, 10, 217, 44))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_Busca = QLineEdit(self.frame_31)
        self.lineEdit_Busca.setObjectName(u"lineEdit_Busca")
        self.lineEdit_Busca.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.lineEdit_Busca)

        self.btn_Buscar = QPushButton(self.frame_31)
        self.btn_Buscar.setObjectName(u"btn_Buscar")
        self.btn_Buscar.setMinimumSize(QSize(25, 22))
        self.btn_Buscar.setMaximumSize(QSize(25, 22))
        self.btn_Buscar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"image: url(pesquisa.svg);")


        self.horizontalLayout_8.addWidget(self.btn_Buscar)

        self.frame_32 = QFrame(self.alugados)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(220, 30, 130, 34))
        self.frame_32.setMinimumSize(QSize(200, 0))
        self.frame_32.setMaximumSize(QSize(130, 16777215))
        self.frame_32.setStyleSheet(u"border:0px\n"
"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_32)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titulo = QLabel(self.frame_32)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setStyleSheet("font-size: 20px")

        self.verticalLayout.addWidget(self.titulo)

        self.horizontalLayout_7.addWidget(self.alugados)

        self.horizontalLayout_6.addWidget(self.frame_30)

        self.stackedWidget_2.addWidget(self.c_historico)

        self.horizontalLayout_3.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Locar Aluguel de Carros", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.email_login.setInputMask("")
        self.email_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"z\u00e9@locar.com", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.senha_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"senha", None))
        self.btn_home.setText("")
        self.btn_c_carro.setText("")
        self.btn_c_funcionario.setText("")
        self.btn_c_aluguel.setText("")
        self.btn_c_cliente.setText("")
        self.btn_logout.setText("")
        self.label_VALOR.setText(QCoreApplication.translate("MainWindow", u"Valor Di\u00e1ria", None))
        self.label_ANO.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.label_MODELO.setText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.BTN_CANCELAR.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.BTN_CONFIRMAR.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.label_DESCRIAO.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.label_2PLACA.setText(QCoreApplication.translate("MainWindow", u"Placa", None))
        self.BTN_CANCELAR_2.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.BTN_CONFIRMAR_2.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.label_EMAIL.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_NOME.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_CPF.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_Perfil.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.comboBox_Perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None))
        self.comboBox_Perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.BTN_CANCELAR_3.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.BTN_CONFIRMAR_3.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))
        self.label_Perfil_2.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None))
        self.comboBox_Perfil_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Cr\u00e9dito", None))
        self.comboBox_Perfil_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Debito", None))
        self.comboBox_Perfil_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Dinheiro", None))

        self.data_entrega_label.setText(QCoreApplication.translate("MainWindow", u"Data Entrega", None))
        self.data_retirada_label.setText(QCoreApplication.translate("MainWindow", u"Data Retirada", None))

        self.cpf_aluguel_label.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.carro.setText(QCoreApplication.translate("MainWindow", u"Carro", None))
      
        self.label_CPF_cliente.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_NOME_cliente.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.BTN_CANCELAR_4.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.BTN_CONFIRMAR_4.setText(QCoreApplication.translate("MainWindow", u"CONFIRMAR", None))

        ___qtablewidgetitem = self.tabela.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CLIENTE", None));
        ___qtablewidgetitem1 = self.tabela.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CARRO", None));
        ___qtablewidgetitem2 = self.tabela.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"RETIRADA", None));
        ___qtablewidgetitem3 = self.tabela.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ENTREGA", None));
        self.lineEdit_Busca.setText("")
        self.lineEdit_Busca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btn_Buscar.setText("")
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"LISTA DE ALUGADOS", None))
    # retranslateUi