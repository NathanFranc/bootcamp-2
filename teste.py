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