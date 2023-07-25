import os

a = input("Insira o primeiro número que deseja utilizar: ")
b = input("Insira o segundo número que deseja utilizar: ")
c = input("Insira o terceiro número que deseja utilizar: ")
d = input("Insira o quarto número que deseja utilizar: ")
e = input("Insira o quinto número que deseja utilizar: ")
print("")

num = [a, b, c, d, e]
print("")

for N in num:
	print(N)

if a > b and a > c and a > d and a > e:
	print(f"O maior número é {a}")
elif b > a and b > c and b > d and b > e:
	print(f"O maior número é {b}")
elif c > a and c > b and c > d and c > e:
	print(f"O maior número é {c}")
elif d > a and d > b and d > c and d > e:
	print(f"O maior número é {d}")
else:
	print(f"O maior número é {e}")
	
    
if a < b and a < c and a < d and a < e:
	print(f"O menor número é {a}")
elif b < a and b < c and b < d and b < e:
	print(f"O menor número é {b}")
elif c < a and c < b and c < d and c < e:
	print(f"O menor número é {c}")
elif d < a and d < b and d < c and d < e:
	print(f"O menor número é {d}")
else:
	print(f"O menor número é {e}")

os.system("pause")