from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
  def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
    super().__init__(parent, *args, **kwargs)
    
    self.cw = QWidget()
    self.vLayout = QVBoxLayout()
    self.cw.setLayout(self.vLayout)
    self.setCentralWidget(self.cw)
    
    self.setWindowTitle('Calculadora')
    
    # Definindo um tamanho fixo para a janela.
  def adjustFixedSixe(self):
    self.adjustSize()
    self.setFixedSize(self.width(), self.height())
    
  def addWidget(self, widget: QWidget):
    self.vLayout.addWidget(widget)