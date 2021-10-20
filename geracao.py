birth = int(input("Digite o ano de nascimento: "))

if birth <= 1964:
    print("Baby Boomer")
elif birth <= 1979:
    print("Geração X")
elif birth <= 1994:
    print("Geração y")
else:
    print("Geração Z")