# #### Inteiros (`int`)

import math

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
primeiro = int(input("inserir numero inteiro: "))
segundo = int(input("inserir outro numero inteiro: "))

resultado = primeiro + segundo 

print(resultado)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero1 = int(input("inserir numero inteiro: "))
resto = numero1 % 5
print("O resto da divisão por 5 é: ", resto)


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numer1 = int(input("inserir numero inteiro: "))
numer2 = int(input("inserir outro numero inteiro: "))
resultado = numer1 * numer2
print("o resultado da multiplicação é:",resultado)



# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_01 = int(input("inserir um numero inteiro: "))
numero_02 = int(input("inserir outro numero inteiro: "))
resultado = numero_01 // numero_02 
print(resultado)
 
 
 
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("inserir numero inteiro: "))
quadrado = numero ** 2
print("o quadrado é:",quadrado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero1 = float(input("inserir numero flutuante: "))
numero2 = float(input("inserir segundo numero flutuante: "))
resultado = numero1 + numero2
print("resultado:",resultado)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

numero = float(input("inserir pimeiro numero flutuante:"))
numero2 = float(input("inserir segundo numero flutuante: "))
resultado = (numero + numero2) / 2
print("resultado da media: ", resultado)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("inserir numero base: "))
expoente  = float(input("inserir expoente: "))
resultado = base ** expoente
print(f"resultado: {resultado: .2f}")


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
try:
     celsius = float(input("inserir temperatura em celsius: "))
     fahrenhait = (celsius * 9/5) + 32
     print(f"{celsius} equivale {fahrenhait}°F")   
except ValueError:
    print("Erro: Digite apenas numeros !")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

try:  
    raio = float(input("digite o raio: "))
    area = math.pi * (raio ** 2)
    print(f"a area do circulo é: {area:.2f}")   
except ValueError:
         print("Erro: digite apenas numeros !")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
print("texto em mainsculo:",texto.upper())


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
texto = input("Digite o seu nome completo: ")
print("texto em minusculo: ",texto.lower())


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no finfrase
frase = input("insira uma frase : ")
frase_sem_espaços = frase.strip
print(" frase sem espaços extras:", frase_sem_espaços)


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_do_usuario = input("Insira uma data no formato dd/mm/aaa: ")
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"o elemento 1 e o: {lista_de_dia_mes_ano[0]}")
print(f"o elemento 2 e o: {lista_de_dia_mes_ano[1]}")
print(f"o elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input(" digite sua primeira string: ")
string2 = input(" digite sua segunda string: ")

resultado = string1 + " " + string2
print("strings conctnação", resultado)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

exprt1 = input("insira a primeira expressão booleana (true/false): ").lower() == 'true'
exprt2 = input("insira uma segunda expressão booleana (ture/false): ").lower() == 'true'

resultado = exprt1 and exprt2 

print(f"resultado do AND logico: {resultado}")


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR
valor1 = input("insira o primeiro valor booleana (true/false): ").lower() == 'true'
valor2 = input("insira o segundo valor booleana (true/false): ").lower() == 'true'

resultado = valor1 or valor2 

print(f"resultado do OR logico: {resultado}")


# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

entrada = input("insira o primeiro valor booleana (true/false): ").lower()

valor_booleano = entrada == 'true'
valor_invertido = not valor_booleano

print(f"valor original: {valor_booleano}")
print(f"valor invertido: {valor_invertido}")


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))

print(f"\n{n1} == {n2}? {n1 == n2}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.


n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))

print(f"\n{n1} != {n2}? {n1 != n2}")



# #### try-except e if

# 21: Conversor de Temperatura
temperatura = float(input("Digite a temperatura: "))  
escala = input("Converter para (C/F): ").upper()  # Converte para maiúsculo  

if escala == "C":  
       convertida = (temperatura - 32) * 5/9  
       print(f"{temperatura}°F → {convertida:.1f}°C")  # :.1f arredonda para 1 decimal  
elif escala == "F":  
       convertida = (temperatura * 9/5) + 32  
       print(f"{temperatura}°C → {convertida:.1f}°F")  
else:  
       print("Escala inválida. Use 'C' ou 'F'.")



# 22: Verificador de Palíndromo

texto = input("Digite uma palavra/frase: ").lower()  # Converte para minúsculas
texto_limpo = texto.replace(" ", "").replace(",", "").replace(".", "")  # Remove espaços e pontuações

if texto_limpo == texto_limpo[::-1]:  # Compara com a versão invertida
    print("✅ É um palíndromo!")
else:
    print("❌ Não é um palíndromo.")


# 23: Calculadora Simples

# Recebe os números e a operação  
try:  
    num1 = float(input("Digite o primeiro número: "))  
    operador = input("Digite a operação (+ - * /): ")  
    num2 = float(input("Digite o segundo número: "))  

    # Realiza a operação  
    match operador:  
        case "+":  
            resultado = num1 + num2  
        case "-":  
            resultado = num1 - num2  
        case "*":  
            resultado = num1 * num2  
        case "/":  
            resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"  
        case _:  
            resultado = "Operação inválida"  

    print(f"Resultado: {resultado}")  

except ValueError:  
    print("Erro: Digite apenas números válidos!")



# 24: Classificador de Números

try:  
    numero = float(input("Digite um número: "))  

    # Classifica positivo/negativo/zero  
    if numero > 0:  
        print("✅ Positivo", end=", ")  
    elif numero < 0:  
        print("✅ Negativo", end=", ")  
    else:  
        print("✅ Zero", end=", ")  

    # Classifica par/ímpar (apenas se for inteiro)  
    if numero.is_integer():  
        if int(numero) % 2 == 0:  
            print("par")  
        else:  
            print("ímpar")  
    else:  
        print("(não inteiro)")  

except ValueError:  
    print("❌ Erro: Digite apenas números!")


# 25: Conversão de Tipo com Validação

def converter_para_numero(mensagem, tipo=float):  
    while True:  
        entrada = input(mensagem)  
        try:  
            numero = tipo(entrada.replace(",", "."))  # Substitui vírgula por ponto  
            return numero  
        except ValueError:  
            print(f"Erro: '{entrada}' não é um {tipo._name_} válido. Tente novamente!")  

# Exemplo de uso:  
numero = converter_para_numero("Digite um número (aceita vírgula ou ponto): ", float)  
print(f"✅ Número convertido: {numero} (tipo: {type(numero)._name_})")