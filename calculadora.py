# -*- coding: utf-8 -*- 
"""
Calculadora v2
Autora: Maria Caroline Sousa
Função: fazer cálculos: soma, divisão, multiplicação, divisão e exponenciação
"""

print("------ Calculadora v2.0 -------")

sair = False

while sair == False:
	
	num1 = input("Digite o primeiro Número: ")
	num1 = int(num1)
	operador = input("Digite o Operador (+ - * / ** ) :")
	num2 = input("Digite o segundo Número: ")
	num2 = int(num2)

	# + Soma
	if operador == "+":
		operacao = num1 + num2

	# - Subtração
	if operador == "-":
		operacao = num1 - num2

	# / Divisão
	if operador == "/":
		operacao = num1 / num2

	# * Multiplicação
	if operador == "*":
		operacao = num1 * num2

	# ** Exponenciação
	if operador == "**":
		operacao = num1 ** num2

	print("Resultado: ")
	print(operacao)

	teste = input("Deseja sair? (s/n): ")
	if teste == "s":
		sair = True