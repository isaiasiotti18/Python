from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

class Display(QLineEdit):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.configStyle()
    
  def configStyle(self):
    margins = [4, 4, 4, 4]
    
    self.setStyleSheet('font-size: 24px;')
    self.setMinimumHeight(24*1.8)
    self.setMinimumWidth(350)
    self.setAlignment(Qt.AlignmentFlag.AlignRight)
    self.setTextMargins(*margins)