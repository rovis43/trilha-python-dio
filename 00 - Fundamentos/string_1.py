nome = "gUIlherME"

# print(nome.upper())
# print(nome.lower())
# print(nome.title())

texto = "  Olá mundo!    "

# print(texto + ".")
# print(texto.strip() + ".")
# print(texto.rstrip() + ".")
# print(texto.lstrip() + ".")

menu = "Java"

# print("####" + menu + "####")
# print(menu.center(20))
# print(menu.center(20, "#"))
# print("-".join(menu))

valor = 100
numero_saques = 2


# print("{:>20}".format(valor))
print("Saque: R${:<10.2f}".format(valor) + "{:>30}⁰ saque".format(numero_saques))

# # assigning strings to the variables 
# left_alignment = "Saque: R$ {valor:.2f}"
# center_alignment = "Centered Text"
# right_alignment = "Right Text"

# # printing out aligned text 
# print(f"{left_alignment : <20}{center_alignment : ^15}{right_alignment : >20}") 
