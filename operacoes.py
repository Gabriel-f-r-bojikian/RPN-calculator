def soma(lvalue, rvalue):
  return lvalue + rvalue

def subtrai(lvalue, rvalue):
  return lvalue - rvalue

def multiplica(lvalue, rvalue):
  return lvalue*rvalue

def divide(lvalue, rvalue):
  if rvalue != 0:
    return lvalue / rvalue
  else:
    return "Erro, divisão por zero"

def elevaEsqueroAoDireito(lvalue, rvalue):
  return lvalue**rvalue

def fazConta(lvalue, rvalue, operacao):
  if operacao == "+":
    return soma(lvalue, rvalue)

  elif operacao == "-":
    return subtrai(lvalue, rvalue)

  elif operacao == "*":
    return multiplica(lvalue, rvalue)
  
  elif operacao == "/" or operacao == "%":
    return divide(lvalue, rvalue)

  elif operacao == "^":
    return elevaEsqueroAoDireito(lvalue, rvalue)
  #Esta função não está retornando esta mensagem de erro quando ocorre operador invalido
  #Preciso usar try and except para corrigir isto
  else:
    return "erro, operacao invalida"