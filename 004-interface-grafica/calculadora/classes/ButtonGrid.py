from classes.Button import Button
from classes.Display import Display

from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot

from utils import isEmpty, isNumOrDot

class ButtonGrid(QGridLayout):
  def __init__(self, display: Display, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    
    self.createButton()
    self.display = display

  def createButton(self):
  # Define your button labels here
    buttonLabels = [
      ['C', '◀', '^', '/'],
      ['7', '8', '9', '*'],
      ['4', '5', '6', '-'],
      ['1', '2', '3', '+'],
      ['',  '0', '.', '='],
    ]

    # Create and add buttons to the grid
    for rowNumber, rowData in enumerate(buttonLabels):
      for colNumber, buttonText in enumerate(rowData):
        button = Button(buttonText)
        
        if not isNumOrDot(buttonText) and not isEmpty(buttonText):
          button.setStyleSheet('background-color: #023047;')
        
        self.addWidget(button, rowNumber, colNumber)
        buttonSlot = self.makeButtonDisplaySlot(
          self.insertButtonTextToDisplay,
          button
        )
        button.clicked.connect(buttonSlot)
  def makeButtonDisplaySlot(self, func, *args, **kwargs):
    @Slot(bool)
    def realSlot(_):
      func(*args, **kwargs)
    return realSlot

  def insertButtonTextToDisplay(self, button: Button):
    buttonText = button.text()
    self.display.insert(buttonText)
