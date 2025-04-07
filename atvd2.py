while True:
    operacao = input('digite uma operação: (+ / - / *)')

    if operacao == '+':
        numero1 = int(input('digite o primeiro numero que deseja somar:'))
        numero2 = int(input('digite o segundo numero que deseja somar:'))

        print(f"o resultado da operação é: {numero1 + numero2}")
        continue

    elif operacao == '-':
        numero1 = int(input('digite o primeiro numero que deseja subtrair:'))
        numero2 = int(input('digite o segundo numero que deseja subtrair:'))

        print(f"o resultado da operação é: {numero1 + numero2}")
        continue

    elif operacao == '*':
        numero1 = int(input('digite o primeiro numero que deseja multiplicar:'))
        numero2 = int(input('digite o segundo numero que deseja multiplicar:'))

        print(f"o resultado da operação é: {numero1 + numero2}")
        continue
