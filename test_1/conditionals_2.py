ventas  = 67_000

# if ventas < 80_000:
#     print("las ventas no fueron suficientes menores a 80_000")
# elif ventas < 75_000:
#     print("las ventas no fueron suficientes menores a 75_000")
# elif ventas < 65_000:
#     print("las ventas no fueron suficientes menores a 65_000")
# else:
#     print("las ventas fueron suficientes")

sku = "jack daniels"
if ventas < 65_000 and sku == "jack daniels" :
    print("las ventas no fueron suficientes menores a 80_000")
    count = 1
elif ventas < 75_000:
    print("las ventas no fueron suficientes menores a 75_000")
elif ventas < 80_000:
    print("las ventas no fueron suficientes menores a 65_000")
else:
    print("las ventas fueron suficientes")

nombre = input("Ingresa tu nombre: ")

print(f"{nombre}")

