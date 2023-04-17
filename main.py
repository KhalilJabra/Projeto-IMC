altura = float(input("Qual é a sua altura em cm: "))
peso = float(input("Qual é o seu peso em kg: "))

IMC = peso/(altura/100)**2

print(IMC)


if IMC < 18.5:
    print(f"Seu IMC é de {IMC}, e é classificado como "
          f"magreza")
elif IMC>= 18.5 and IMC <  24.9:
        print(f"Seu IMC é de {IMC}, e é classificado como "
              f"normal")
elif IMC>= 25 and IMC < 29.9:
        print(f"Seu IMC é de {IMC}, e é classificado como "
              f"sobrepeso")
elif IMC>= 30 and IMC < 39.9:
    print(f"Seu IMC é de {IMC}, e é classificado como "
          f"obesidade")
else:
    print("Cuidado com a sua saúde, obesidade acima da média entre 30 a 39.9!")
