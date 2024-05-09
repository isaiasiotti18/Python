import stat
import sys

import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
central = QWidget()
window.setCentralWidget(central)

button = QPushButton('Enviar')
button.setStyleSheet('font-size: 40px;')

btn02 = QPushButton('Enviar 02')
btn02.setStyleSheet('font-size: 40px;')

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(btn02)

central.setLayout(layout)

print(PySide6.__version__)
print(PySide6.QtCore.__version__)

status_bar = window.statusBar()
status_bar.showMessage('Version: 1.3.2')

def slot_example(status_bar):
  status_bar.showMessage('O meu slot foi executado')

menu = window.menuBar()
firstMenu = menu.addMenu('help')
firstAction = firstMenu.addAction('FAQ')
firstAction.triggered.connect(
  lambda: slot_example(status_bar)
)

window.show()

app.exec()
