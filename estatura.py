est1 = float(input("Digite a primeira estatura: "))
est2 = float(input("Digite a segunda estatura: "))
est3 = float(input("Digite a terceira estatura: "))

if est1 == est2 or est1 == est3 or est2 == est3:
    print("Há, pelo menos, 2 pessoas com a mesma estatura")

elif est1 > est2 and est1 > est3:
    print("Maior estatura:", est1)

elif est2 > est1 and est2 > est3:
    print("Maior estatura:", est2)

else:
    print("Maior estatura:", est3)
