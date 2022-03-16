from email.mime import image
import sys
from ctypes import windll
from ui_login_locar import *
import sqlite3

class MainWindow(QMainWindow):
    
    adm = None
       
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        self.ui.email_login.returnPressed.connect(lambda: self.ui.senha_login.setFocus())
        self.ui.senha_login.returnPressed.connect(self.fazLogin)

        self.ui.btn_home.clicked.connect(self.limpaCampos)
        self.ui.btn_home.clicked.connect(self.carregarHistorico)

        self.ui.btn_c_carro.clicked.connect(self.limpaCampos)
        self.ui.btn_c_carro.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_carro))
        
        self.ui.btn_c_funcionario.clicked.connect(self.verificaPerfil)
    
        self.ui.btn_c_aluguel.clicked.connect(self.limpaCampos)
        self.ui.btn_c_aluguel.clicked.connect(self.carregarCarro)
        self.ui.btn_c_aluguel.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_aluguel))

        self.ui.btn_c_cliente.clicked.connect(self.limpaCampos)
        self.ui.btn_c_cliente.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_cliente))
        
        self.ui.btn_logout.clicked.connect(self.fazLogout)

        self.ui.BTN_CONFIRMAR.clicked.connect(self.cadastroCarro)
        self.ui.BTN_CANCELAR.clicked.connect(self.limpaCampos)
        self.ui.BTN_CONFIRMAR_2.clicked.connect(self.cadastroFuncionario)
        self.ui.BTN_CANCELAR_2.clicked.connect(self.limpaCampos)
        self.ui.BTN_CONFIRMAR_3.clicked.connect(self.cadastroAluguel)
        self.ui.BTN_CANCELAR_3.clicked.connect(self.limpaCampos)
        self.ui.BTN_CONFIRMAR_4.clicked.connect(self.cadastroCliente)
        self.ui.BTN_CANCELAR_4.clicked.connect(self.limpaCampos)
        self.ui.btn_Buscar.clicked.connect(self.carregarHistorico)
        
        self.ui.lineEdit_Busca.returnPressed.connect(self.carregarHistorico)

        self.ui.tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tabela.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.ui.tabela.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.ui.tabela.horizontalHeader().resizeSection(2, 85)
        self.ui.tabela.horizontalHeader().resizeSection(3, 85)

# limpa campos
    def limpaCampos(self):
        for i in self.ui.stackedWidget.currentWidget().findChildren(QLineEdit):
            i.clear()

        for i in self.ui.stackedWidget.currentWidget().findChildren(QComboBox):
            i.setCurrentIndex(0)
# login    
    def fazLogin(self):
        email = self.ui.validaEmail.validate(self.ui.email_login.text(),0)
        senha = self.ui.senha_login.text()
        try:
            cursor = banco.cursor()
            cursor.execute('select email, senha, perfil from funcionario')
        except sqlite3.Error as erro:
            print('Erro com o banco de dados: ', erro)
            return
        usuarios = cursor.fetchall()
        print(usuarios)
        for usuario in usuarios:
            if usuario[0] == email[1] and usuario[1] == senha:
                self.adm = usuario[2]
                self.limpaCampos()
                self.carregarHistorico()
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
                return
        print('usuario nao encontrado!!!')
# logout
    def fazLogout(self):
        self.adm = None
        self.limpaCampos()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        
#cadastro de carro
    def cadastroCarro(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_carro)
        modelo = self.ui.validaTexto.validate(self.ui.lineEdit_MODELO.text(),0)
        placa = self.ui.validaPlaca.validate(self.ui.lineEdit_PLACA.text(),0)
        ano = self.ui.validaAno.validate(self.ui.lineEdit_ANO.text(),0)
        descricao = self.ui.validaTexto.validate(self.ui.lineEdit_4DESCRIAO.text(),0)
        valor_diaria = self.ui.validaInteiro.validate(self.ui.lineEdit_VALOR.text(),0)
        args = (modelo[1],placa[1],ano[1],descricao[1],valor_diaria[1])
        try:
            cursor = banco.cursor()
            cursor.execute('insert into veiculo(modelo, placa, ano, descricao, valor)values(?,?,?,?,?)', args)
            banco.commit()
            print('sucesso!')
        except sqlite3.Error as erro:        
            print('Erro com o banco de dados: ', erro)
            return
#verifica perfil
    def verificaPerfil(self):
        if self.adm:
           self.limpaCampos()
           self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_funcionario)

#cadastro de funcionario
    def cadastroFuncionario(self):
        nome = self.ui.validaNome.validate(self.ui.lineEdit_NOME.text(),0)
        cpf = self.ui.validaCPF.validate(self.ui.lineEdit_CPF.text(),0)
        email = self.ui.validaEmail.validate(self.ui.lineEdit_EMAIL.text(),0)
        senha = self.ui.validaTexto.validate(self.ui.lineEdit_Senha.text(),0)
        perfil = self.ui.comboBox_Perfil.currentIndex() 

        args = (nome[1],cpf[1],email[1],senha[1],perfil)
        print(args)
        try:
            cursor = banco.cursor()
            cursor.execute('insert into funcionario(nome,cpf,email,senha,perfil)values(?,?,?,?,?)', args)
            banco.commit()
            print('sucesso!')
        except sqlite3.Error as erro:        
            print('Erro com o banco de dados: ', erro)
            return
#carrega carro
    def carregarCarro(self):
        try:
            cursor = banco .cursor()
            cursor.execute('select modelo, valor from veiculo')
            print('sucesso!')
        except sqlite3.Error as erro:
            print('Erro com o banco e dados: ', erro)
            return
        
        self.ui.data_retirada.setDate(QDate.currentDate())
        self.ui.data_retirada.setSelectedSection(QDateEdit.NoSection)

        self.ui.data_entrega.setDate(QDate.currentDate())
        self.ui.data_entrega.setSelectedSection(QDateEdit.NoSection)

        ##################### propriedade intelectual DIEGO #####################
        modelos = cursor.fetchall()
        if self.ui.comboBox.count() == 0:
            for modelo in modelos:
                self.ui.comboBox.addItem(f"{modelo[0]} R${modelo[1]:.2f}")
        elif len(modelos) > self.ui.comboBox.count():
            dif = self.ui.comboBox.count() - len(modelos)
            for modelo in modelos[dif:]:
                self.ui.comboBox.addItem(f"{modelo[0]} R${modelo[1]:.2f}")
        ##########################################################################

  #busca cliente      
    def buscaCliente(self, cpf):
        try:
            cursor = banco.cursor()
            cursor.execute('select cpf, nome, id_cliente from cliente')
        except sqlite3.Error as erro:
            print('Erro com o banco de dados: ', erro)
            return
        
        clientes = cursor.fetchall()
        for cliente in clientes:
            if cliente[0] == cpf[1]:
                print(f'cliente: {cliente[1]}')
                return cliente[2]
        
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_cliente)
  #busca veiculo
    def buscaVeiculo(self, nome):
        nome = nome.split()[0]
        try:
            cursor = banco.cursor()
            cursor.execute('select modelo, id_veiculo from veiculo')
        except sqlite3.Error as erro:
            print('Erro com o banco de dados: ', erro)
            return
        veiculos = cursor.fetchall() 
        for veiculo in veiculos:
            if veiculo[0] == nome:
                print(f'veiculo: {veiculo[1]}')
                return veiculo[1]

#cadastro aluguel 
    def cadastroAluguel(self):
        cpf = self.ui.validaCPF.validate(self.ui.cpf_aluguel.text(),0)
                
        data_retirada = self.ui.data_retirada.text()
        data_entrega = self.ui.data_entrega.text()
        pagamento = self.ui.comboBox_Perfil_2.currentIndex()

        idC = self.buscaCliente(cpf)
        idV = self.buscaVeiculo(self.ui.comboBox.currentText())
        
        if self.ui.comboBox_Perfil_2.currentIndex() == 0:
            pagamento = "credito"
        elif self.ui.comboBox_Perfil_2.currentIndex() == 1:
            pagamento = "debito"
        else:
            pagamento = "dinheiro"

        args = (data_retirada, data_entrega, pagamento, idC, idV)
        print(args)
        try:
            cursor = banco.cursor()
            cursor.execute('insert into aluguel(data_retirada, data_entrega, pagamento, fk_cliente, fk_veiculo) values (?,?,?,?,?)', args)
            banco.commit()
            print('sucesso!')
        except sqlite3.Error as erro:        
            print('Erro com o banco de dados: ', erro)
            return
#carregar historico
    def carregarHistorico(self):
        
        txt = self.ui.lineEdit_Busca.text().lower()
        if txt == '':		
            query = '''select cliente.nome,veiculo.modelo, aluguel.data_retirada, aluguel.data_entrega from aluguel left join veiculo on
                        aluguel.fk_veiculo = veiculo.id_veiculo left join cliente on cliente.id_cliente = aluguel.fk_cliente '''
        else:
            query = f'''select cliente.nome,veiculo.modelo, aluguel.data_retirada, aluguel.data_entrega from aluguel left join veiculo on
                        aluguel.fk_veiculo = veiculo.id_veiculo left join cliente on cliente.id_cliente = aluguel.fk_cliente WHERE cliente.nome 
                        LIKE "%{txt}%" OR veiculo.modelo LIKE "%{txt}%" OR aluguel.data_retirada LIKE "%{txt}%" OR aluguel.data_entrega LIKE "%{txt}%" '''

        try:
            cursor = banco.cursor()
            cursor.execute(query)
        except sqlite3.Error as erro:
            print('Erro com o banco de dados: ', erro)
            return
        historicos = cursor.fetchall()
        
        self.ui.tabela.setRowCount(len(historicos))
        for lin, historico in enumerate(historicos):
            for col, dado in enumerate(historico):
                self.ui.tabela.setItem(lin, col, QTableWidgetItem(dado))
                self.ui.tabela.item(lin, col).setTextAlignment(Qt.AlignCenter)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.c_historico)
#cadastro cliente
    def cadastroCliente(self):
        NOME = self.ui.validaNome.validate(self.ui.lineEdit_NOME_cliente.text(),0)
        CPF = self.ui.validaCPF.validate(self.ui.lineEdit_CPF_cliente.text(),0)
        args = (NOME[1], CPF[1])
        try:
            cursor = banco.cursor()
            cursor.execute('insert into cliente (nome,cpf) values(?,?)', args)
            banco.commit()
            print('')
        except sqlite3.Error as erro:
            print('Erro com o banco de dados: ', erro)
            return

if __name__ == '__main__':
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    banco = sqlite3.connect('db/locar.db')

    app = QApplication()
    main = MainWindow()
    app.exec()
    app.setWindowIcon(QIcon('carro.svg'))
    sys.exit(banco.close())