from classes.Button import Button
from classes.Display import Display
from classes.Info import Info

from PySide6.QtWidgets import QGridLayout
from PySide6.QtCore import Slot

from utils import isEmpty, isNumOrDot, isValidNumber

class ButtonGrid(QGridLayout):
  def __init__(self, display: Display, info: Info, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
  
    self.display = display
    self.info = info
    
    self._equation = ''
    self._equationInitialValue = 'Sua Conta'
    self._leftNumber = None
    self._rightNumber = None
    self._operation = None
    
    self._equation = self._equationInitialValue
    
    self.createGridOfButtons()
    
  @property
  def equation(self):
    return self._equation
  
  @equation.setter
  def equation(self, value):
    self._equation = value
    self.info.setText(value)

  def createGridOfButtons(self):
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
          self.configSpecialButton(button)
        
        self.addWidget(button, rowNumber, colNumber)
        buttonSlot = self.makeButtonDisplaySlot(
          self.insertButtonTextToDisplay,
          button
        )
        self.connectButtonClicked(button, buttonSlot)
  
  def connectButtonClicked(self, button, slot):
    button.clicked.connect(slot)
    
  def operatorClicked(self, button: Button):
    buttonText = button.text()
    displayText = self.display.text()
    self.display.clear()
    
    if not isValidNumber(displayText) and self._leftNumber is None:
      return
    
    if self._leftNumber is None:
      self._leftNumber = float(displayText)
      
    self._operation = buttonText
    self.equation = f'{self._leftNumber} {self._operation} ??' 
    
  def configSpecialButton(self, button: Button):
    buttonText = button.text()
    
    if buttonText == 'C':
      buttonSlot = self.makeButtonDisplaySlot(self.display.clear)
      self.connectButtonClicked(button, buttonSlot)
      self._leftNumber = None
      self._rightNumber = None
      self._operation = None
      self.equation = self._equationInitialValue
    
    if buttonText in '+-*/':
      self.connectButtonClicked(
        button,
        self.makeButtonDisplaySlot(self.operatorClicked, button)
      )
  
  def makeButtonDisplaySlot(self, func, *args, **kwargs):
    @Slot(bool)
    def realSlot(_):
      func(*args, **kwargs)
    return realSlot

  def insertButtonTextToDisplay(self, button: Button):
    buttonText = button.text()
    newDisplayValue = self.display.text() + buttonText
    
    if not isValidNumber(newDisplayValue):
      return
    
    self.display.insert(buttonText)
