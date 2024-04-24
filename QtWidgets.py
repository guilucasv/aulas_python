# QWidget e QLayout de PySide6.QtWidgets
# -> QApplication
#   -> QMainWindow (window - setCentralWidget)
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget

app = QApplication(sys.argv)

window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)

botao = QPushButton('Login')
botao.setStyleSheet('font-size: 40px;')

botao2 = QPushButton('Senha')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Clique para entrar')
botao3.setStyleSheet('font-size: 40px;')


layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage('O slot foi executado.')

def outro_slot(checked):
    print('Está marcado?', checked)

# Status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mensagem de teste status bar')

# MenuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Configurações')
segunda_acao = primeiro_menu.addAction('Sair')
segunda_acao.triggered.connect(lambda: slot_example(status_bar))


segunda_acao = primeiro_menu.addAction('Visualizar')
segunda_acao.setCheckable(True)
segunda_acao.toggled.connect(outro_slot)


window.show() 
app.exec()  # O loop da aplicação