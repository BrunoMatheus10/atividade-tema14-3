# Função para somar dois números
def soma(a, b):
    return a + b

# Função para subtrair o segundo número do primeiro
def subtracao(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicacao(a, b):
    return a * b

# Função para dividir o primeiro número pelo segundo
# Verifica se o divisor não é zero para evitar erro
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida"

# Leitura dos valores inteiros do usuário
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

# Exibição dos resultados das operações
print("Soma: ",soma(a, b))
print("Subtração: ",subtracao(a, b))
print("Multiplicação: ",multiplicacao(a, b))
print("Divisão: ",divisao(a, b))
