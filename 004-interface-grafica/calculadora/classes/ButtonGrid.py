from classes.Button import Button
from PySide6.QtWidgets import QGridLayout

from utils import isEmpty, isNumOrDot

class ButtonGrid(QGridLayout):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self.create_buttons()

  def create_buttons(self):
  # Define your button labels here
    button_labels = [
      ['C', '◀', '^', '/'],
      ['7', '8', '9', '*'],
      ['4', '5', '6', '-'],
      ['1', '2', '3', '+'],
      ['',  '0', '.', '='],
    ]

        # Create and add buttons to the grid
    for rowNumber, rowData in enumerate(button_labels):
      for colNumber, buttonText in enumerate(rowData):
          button = Button(buttonText)
          self.addWidget(button, rowNumber, colNumber)
