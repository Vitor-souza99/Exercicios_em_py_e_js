while True:
    num = input("Digite um número para verificar se pertence à sequência de Fibonacci (digite 'sair' para encerrar): ")
    if num == 'sair':
        break
    num = int(num)
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        print(num, "pertence à sequência de Fibonacci.")
    else:
        print(num, "não pertence à sequência de Fibonacci.")
