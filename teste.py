valor1 = input("insira o primeiro valor booleana (true/false): ").lower() == 'true'
valor2 = input("insira o segundo valor booleana (true/false): ").lower() == 'true'

resultado = valor1 or valor2 

print(f"resultado do OR logico: {resultado}")