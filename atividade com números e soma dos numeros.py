import os

numeros = []

soma = 0

for i in range(5):
    num = int(input("Insira um número: "))
    soma += num

print(f"A soma dos números é: {soma}")

os.system("pause")