import sys

import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication(sys.argv)

button = QPushButton('Enviar')
button.setStyleSheet('font-size: 40px;')

btn02 = QPushButton('Enviar 02')
btn02.setStyleSheet('font-size: 40px;')

central = QWidget()

layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(btn02)

central.setLayout(layout)
central.show()

print(PySide6.__version__)
print(PySide6.QtCore.__version__)

app.exec()
