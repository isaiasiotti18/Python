import qdarktheme
import qdarktheme.util
def setupTheme():
  theme = [
    qdarktheme.load_stylesheet(),
    'corner-shape: rounded;'
  ]
  
  return ' '.join(theme)