#Still need to implement a way to parse fractions correctly, like -1/3

def confirmaSeFloat(valor):
  try:
    float(valor)
    return True
  except ValueError:
    return False


class inputStream:

  def __init__(self, operacoesValidas):
    self.operacoesValidas = operacoesValidas
    self.inputStream = []

  def recebeStreamEntrada(self):
    stringEntrada = input(">")
    self.inputStream = stringEntrada.split()

  def separaNumeroDeOperador(self):
    listaNumeros = []
    listaOperadores = []

    for item in self.inputStream:
      if item in self.operacoesValidas:
        listaOperadores.append(item)
      elif confirmaSeFloat(item):
        listaNumeros.append(float(item))

    return listaNumeros, listaOperadores
        

if __name__ == "__main__":

    operadoresAceitos = ["+", "-", "/", "%", "^"]

    fluxo = inputStream(operadoresAceitos)
    saida = []
    numeros = []
    operadores = []

    while True:
      if saida:
        saida.clear()
      if numeros:
        numeros.clear()
      if operadores:
        operadores.clear()

      saida = fluxo.recebeStreamEntrada()
      numeros, operadores = fluxo.separaNumeroDeOperador()

      print("\tNumeros: ", numeros)
      print("\tOperadores: ", operadores)