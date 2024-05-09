from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont

class Button(QPushButton):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configStyle()
  
  def configStyle(self):
    font = self.font()
    font.setPixelSize(24)
    font.setWeight(QFont.Weight.Bold)
    self.setFont(font)