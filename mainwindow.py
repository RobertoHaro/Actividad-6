from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from particulas.listaparticula import ListaParticulas
from particulas.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.myListaParticulas = ListaParticulas()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

    @Slot()
    def click_mostrar(self):
        self.ui.out_plainTextEdit.clear()
        self.ui.out_plainTextEdit.insertPlainText(str(self.myListaParticulas))

    @Slot()
    def click_agregar_inicio(self):
        myId = self.ui.id_spinBox.value()
        myOrigenX = self.ui.origenX_spinBox.value()
        myOrigenY = self.ui.origenY_spinBox.value()
        myDestinoX = self.ui.destinoX_spinBox.value()
        myDestinoY = self.ui.destinoY_spinBox.value()
        myVelocidad = self.ui.velocidad_spinBox.value()
        myRed = self.ui.red_spinBox.value()
        myGreen = self.ui.green_spinBox.value()
        myBlue = self.ui.blue__spinBox.value()

        myParticula = Particula(myId, myOrigenX, myOrigenY, myDestinoX,myDestinoY,myVelocidad,myRed,myGreen,myBlue)
        self.myListaParticulas.agregar_inicio(myParticula)

    @Slot()
    def click_agregar_final(self):
        myId = self.ui.id_spinBox.value()
        myOrigenX = self.ui.origenX_spinBox.value()
        myOrigenY = self.ui.origenY_spinBox.value()
        myDestinoX = self.ui.destinoX_spinBox.value()
        myDestinoY = self.ui.destinoY_spinBox.value()
        myVelocidad = self.ui.velocidad_spinBox.value()
        myRed = self.ui.red_spinBox.value()
        myGreen = self.ui.green_spinBox.value()
        myBlue = self.ui.blue__spinBox.value()

        myParticula = Particula(myId, myOrigenX, myOrigenY, myDestinoX,myDestinoY,myVelocidad,myRed,myGreen,myBlue)
        self.myListaParticulas.agregar_final(myParticula)