import sys

from env import WINDOW_ICON_PATH

from classes.MainWindow import MainWindow
from classes.Display import Display
from classes.Info import Info
from classes.ButtonGrid import ButtonGrid
from classes.Button import Button

from classes.Styles import setupTheme

from PySide6.QtWidgets import QApplication, QGridLayout
from PySide6.QtGui import QIcon

if __name__ == '__main__':
  
  app = QApplication(sys.argv)
  
  theme = setupTheme()
  
  window = MainWindow()
  
  icon = QIcon(str(WINDOW_ICON_PATH))
  window.setWindowIcon(icon)
  app.setWindowIcon(icon)

  info = Info('80 + 80 = 160')
  window.addWidget(info)
  
  display = Display()
  window.addWidget(display)
  
  buttonGrid = ButtonGrid(display)
  
  gridLayout = QGridLayout()
  
  window.vLayout.addLayout(buttonGrid)
  
  app.setStyleSheet(theme)
  
  window.adjustFixedSixe()

  window.show()
  
  app.exec()