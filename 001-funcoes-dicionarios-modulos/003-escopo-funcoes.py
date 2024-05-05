x = 1

def escopo():
  def other():
    x = 'outro X'
    print(x)
  
  other()
  print(x)

escopo()

print(x)

other() # VAI DA ERRO...