""" 1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.

lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ['Kaike', 'Vitória', 'Welton', 'Cintia']
lista_ano = [2007, 2025]

2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista_numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numeros in lista_numero: 
    print(numeros)

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
    soma = 0

    for numero in range(1, 11):
        if numero % 2 != 0:  # Verifica se o número é ímpar
            soma += numero

    print("A soma dos números ímpares de 1 a 10 é:", soma)

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

    for numero in range(10, 0, -1):
        print (numero)

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

    
6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

        numeros = [10, 5, 3, 7, 2]
        soma = 0

        try:
            for num in numeros:
                soma += num
            print("Soma dos números:", soma)
        except Exception as e:
            print("Ocorreu um erro:", e)

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

    valores = [8, 6, 10, 7]

    try:
        media = sum(valores) / len(valores)
        print("Média dos valores:", media)
    except ZeroDivisionError:
        print("Erro: a lista está vazia, não é possível dividir por zero.")

"""

