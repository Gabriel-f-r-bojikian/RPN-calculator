#Preciso consertar o pau que dá quando eu entro com token inválido
#Preciso descobrir como printar a pilha sem modificar ela e, se possível, sem copiar ela
#Ainda é necessário simplificar as funções para o código ficar mais bonito

#Para o futuro: adicionar números complexos e constantes simbólicas como pi ou e

from queue import LifoQueue
import operacoes as op
import entrada as entry

#Ainda não sei como quero tratar o overflow da pilha
def montaPilhaNumeros(listaNumeros):
  for numero in listaNumeros:
    if not pilhaDeNumeros.full():
      pilhaDeNumeros.put(numero)

def montaPilhaOperacoes(listaOperacoes):
  for operacao in listaOperacoes:
    if not pilhaDeOperacoes.full():
      pilhaDeOperacoes.put(operacao)

pilhaDeNumeros = LifoQueue(maxsize = 20)
pilhaDeOperacoes = LifoQueue(maxsize = 20)

operadoresAceitos = ["+", "-", "/", "%", "*", "^"]

fluxo = entry.inputStream(operadoresAceitos)

while not pilhaDeNumeros.full() and not pilhaDeOperacoes.full():
  
  fluxo.recebeStreamEntrada()
  numeros, operacoes = fluxo.separaNumeroDeOperador()

  montaPilhaNumeros(numeros)
  montaPilhaOperacoes(operacoes)

  valorDireito = pilhaDeNumeros.get()
  valorEsquerdo = pilhaDeNumeros.get()
  operacao = pilhaDeOperacoes.get()

  resultado = op.fazConta(valorEsquerdo, valorDireito, operacao)
  
  print("")
  print("\t= ", resultado, "\n")